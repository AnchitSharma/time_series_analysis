import pandas as pd
df = pd.read_csv('appl.csv', parse_dates=["Date"], index_col='Date')





type(df.Date[0])

# preprocessing of data

df = df.rename(columns={' Close/Last': 'Close', ' Volume':'Volume', ' Open':'Open', ' High':'High', ' Low':'Low'})

df.Close = df.Close.str.replace('$', '')
df.Close = df.Close.str.strip()
df.Close = df.Close.astype("float32")

df.Open = df.Open.str.replace('$', '')
df.Open = df.Open.str.strip()
df.Open = df.Open.astype("float32")

df.High = df.High.str.replace('$', '')
df.High = df.High.str.strip()
df.High = df.High.astype("float32")

df.Low = df.Low.str.replace('$', '')
df.Low = df.Low.str.strip()
df.Low = df.Low.astype("float32")

# retrive data only for Jan 2017

# by supplying the partial index
df["2017-01"]
df["2017-01"].columns
type(df["2017-01"])#['Close/Last']

df["2017-01"].Close.mean()
type(df["2017-01"].loc[:, ' Close/Last'][0])
df["2017-01"].iloc[:, 0]

df["2017-01-07": "2017-01-01"]



# Resampling of data
df.Close.resample('Q').mean().plot(kind="bar")
df.Close.plot()




















