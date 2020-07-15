import pandas as pd
df = pd.read_csv('appl.csv', parse_dates=["Date"], index_col='Date')





type(df.Date[0])

# preprocessing of data

df = df.rename(columns={' Close/Last': 'Close', ' Volume':'Volume', ' Open':'Open', ' High':'High', ' Low':'Low'})

df.Close = df.Close.str.replace('$', '')
df.Close = df.Close.str.strip()

df.Open = df.Open.str.replace('$', '')
df.Open = df.Open.str.strip()


df.High = df.High.str.replace('$', '')
df.High = df.High.str.strip()

df.Low = df.Low.str.replace('$', '')
df.Low = df.Low.str.strip()

