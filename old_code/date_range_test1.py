import pandas as pd

df = pd.read_csv("appl_no_dates.csv")


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





# create date index using date_range function in pandas
#rng = pd.date_range(start="6/1/2017", end="6/30/2017", freq="B")

rng = pd.date_range(start="6/1/2017", periods=df.shape[0], freq="B")

df.set_index(rng, inplace=True)

df.Close.plot()

df["2017-06-01":"2017-06-10"].Close.mean()



# filling the dataset where dates are not available due to saturday and sunday
# using asfreq() method
df.asfreq("D", method="pad")

# similary we can generate for hourly basis
df.asfreq("H", method="pad")

# creating custom data using numpy as pandas

rng = pd.date_range(start="6/1/2017", periods=72, freq="H")

import numpy as np
ts = pd.Series(np.random.randint(1, 10, size=len(rng)), index=rng)

# Handling the holidays
pd.date_range(start="7/1/2017", end="7/21/2017", freq="B")

"""
['2017-07-03', '2017-07-04', '2017-07-05', '2017-07-06',
               '2017-07-07', '2017-07-10', '2017-07-11', '2017-07-12',
               '2017-07-13', '2017-07-14', '2017-07-17', '2017-07-18',
               '2017-07-19', '2017-07-20', '2017-07-21']

this date '2017-07-04' is official holiday is US it can handle using custom B day
"""
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())

# now i can use this usb as a frequency
pd.date_range(start="7/1/2017", end="7/21/2017", freq=usb)



# now create custom calender 

from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday

class myBirthdayCalendar(AbstractHolidayCalendar):
    rules = [
            Holiday("Anchit Birthday", month=1, day=20, observance=nearest_workday)
            ]

myc = CustomBusinessDay(calendar=myBirthdayCalendar())


pd.date_range(start="1/1/2019", end="1/27/2019", freq=myc)


# now for conturies like eyzpt where weekends are on friday and saturday
# use week_mask attribute of CustomBusinessDay

b = CustomBusinessDay(weekmask="Sun Mon Tue Wed Thu")

pd.date_range(start="7/1/2020", end = "7/15/2020", freq=b)











































































