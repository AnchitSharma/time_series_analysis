# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:29:06 2023

@author: anchit_sharma
@Source: https://www.blackarbs.com/blog/time-series-analysis-in-python-linear-models-to-garch/11/1/2016
"""
import os
import sys
import pandas as pd
# !pip install pandas-datareader
import pandas_datareader.data as web
import yfinance as yfin
yfin.pdr_override()

import numpy as np

import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
from statsmodels.tsa.ar_model import AutoReg
import statsmodels.api as sm
import scipy.stats as scs
from arch import arch_model

import matplotlib.pyplot as plt

p = print

# download the data from yahoo finance
end = "2015-01-01"
start = "2007-01-01"


get_px = lambda x: web.get_data_yahoo(x, start=start, end=end)['Adj Close']

symbols = ['SPY', 'TLT', 'MSFT']
# raw adjusted close price
data = pd.DataFrame({sym:get_px(sym) for sym in symbols})
# log returns
lrets = np.log(data/data.shift(1)).dropna()

def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):
        fig = plt.figure(figsize=figsize)
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))
        
        y.plot(ax = ts_ax)
        ts_ax.set_title("Time Series Analysis Plots")
        smt.graphics.plot_acf(y, lags=lags, ax = acf_ax, alpha=0.5)
        smt.graphics.plot_pacf(y, lags=lags, ax= pacf_ax, alpha=0.5)
        sm.qqplot(y, line='s', ax = qq_ax)
        qq_ax.set_title("QQ Plot")
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)
        
        plt.tight_layout()
        
    return

np.random.seed(1)

# plot of discrete white noise
randser = np.random.normal(size=1000)
tsplot(randser, lags=30)

p("Random Series\n -------------\nmean: {:.3f}\nvariance: {:.3f}\nstandard deviation: {:.3f}".format(randser.mean(), randser.var(), randser.std()))

# Random walk with a drift

np.random.seed(1)
n_samples = 1000

x = w = np.random.normal(size=n_samples)
for t in range(n_samples):
    x[t] = x[t-1] + w[t]

_ = tsplot(x, lags=30)

# First difference of simulated Random Walk series

_ = tsplot(np.diff(x), lags=30)

# First difference of SPY prices
_ = tsplot(data['SPY'],lags=30)
_ = tsplot(np.diff(data['SPY']),lags=30)



# simulate linear model
# example Firm ABC sales are -$50 by default and +$25 at every step
# yt = b0 + b1*t + c
w = np.random.randn(100)
y = np.empty_like(w)

b0 = -50.
b1 = 25.

for t in range(len(w)):
    y[t] = b0 + b1*t + w[t]

_ = tsplot(y, lags=30)

# simulate ABC Exponential growth

idx = pd.date_range('2007-01-01', '2012-01-01', freq='M')

# sales increasing at exponential rate
sales = [np.exp(x/12) for x in range(1, len(idx)+1)]

# create dataframe and plot
df = pd.DataFrame(sales, columns=['Sales'], index=idx)

with plt.style.context('bmh'):
    df.plot()
    plt.title('ABC Sales')
    
# ABC log sales
with plt.style.context('bmh'):
    pd.Series(np.log(sales), index=idx).plot()
    plt.title('ABC Log Sales')

# simulate an First order Autoregressive model AR(1) with alpha = 0.6

np.random.seed(1)
n_samples = int(1000)
a= 0.6
x = w = np.random.normal(size=n_samples)

for t in range(n_samples):
    x[t] = a*x[t-1] +w[t]

_ = tsplot(x, lags=30)


# fit an AR(p) model to simulated AR(1) model with alpha = 0.6

mdl = sm.tsa.AutoReg(x, lags=30, trend='n').fit()
from statsmodels.tsa.ar_model import ar_select_order
est_order = ar_select_order(x, maxlag=30, old_names=False)

true_order = 1
p('\nalpha estimate: {:3.5f} | best lag order = {}'.format(mdl.params[0], est_order.model.ar_lags))

p('\ntrue alpha = {} | true order = {}'.format(a, true_order))


mdl.params[0]




