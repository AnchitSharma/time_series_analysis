import pandas as pd

dates = ['2017-01-05 2:30:00 PM', 
         'Jan 5, 2017 14:30:00',
         "01/05/2017",
         "2017.01.05",
         "2017/01/05",
         "20170105"]

pd.to_datetime(dates)

pd.to_datetime("5#1#2017", format="%d#%m#%Y")
               
               
               

               

dates = ['2017-01-05 2:30:00 PM', 
         'Jan 5, 2017 14:30:00',
         "01/05/2017",
         "2017.01.05",
         "2017/01/05",
         "20170105", "abc"]

pd.to_datetime(dates, errors="coerce")

# converting epoch to datetime 
t = 1594830661
dt = pd.to_datetime([t], unit="s")

# converting datetime to epochs
dt.view('int64')


               


























