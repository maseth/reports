import pandas as pd
import datetime as dt

absence = 0.147
df = pd.DataFrame()
df['start'] = [dt.datetime(2018, 5, 1), dt.datetime(2018, 11, 1), dt.datetime(2018, 1, 1)]
df['end'] = [dt.datetime(2018, 11, 30), dt.datetime(2018, 11, 30), dt.datetime(2018, 12, 31) ]
df['hours'] = [1232.0, 176.0, 2088.0]

data_series = list()
for row in df.itertuples():
    time_range = pd.bdate_range(row.start, row.end)
    s = len(time_range)
    data_series += (zip(time_range,  [row.hours/s]*s))

df2 = pd.DataFrame(data_series, columns={'date', 'hours'})
df2 = df2.groupby('date').sum().groupby(pd.Grouper(freq='M')).agg(['sum', 'count'])
df2.columns = ['hours', 'count_days']
people = df2['hours'] / (df2['count_days'] * 8)
df2['people'] = people + (people * absence)
df2.reset_index()

print(df2)
