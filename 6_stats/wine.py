import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

data = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data',
                   sep=r'\s+', parse_dates=[[0, 1, 2]])

def fix_date(orig_date):
    # datetime.date(year, x.month, x.day)
    if orig_date.year > 1989:
        return orig_date + relativedelta(years=-100)
    else:
        return orig_date


data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_date)
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data = data.set_index('Yr_Mo_Dy', drop=True)

is_na_count = data.isnull().sum()
not_na_count = data.notnull().sum()

mean_all_loc_time = data.sum().sum() / data.notna().count().sum()

loc_stats = data.describe(percentiles=[])
data['min'] = data.apply(lambda x: x.min())


day_stats = pd.DataFrame()
day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis=1)
day_stats['mean'] = data.mean(axis=1)
day_stats['std'] = data.std(axis=1)

jan_stats = data.loc[day_stats.index.month == 1].mean()

data_yearly = data.groupby(data.index.year).mean()

data_weekly = data.resample('W').agg(['min', 'max', 'mean', 'std'])
first_52_week = data_weekly.loc[data_weekly.index[1:53], "RPT":"MAL"]

