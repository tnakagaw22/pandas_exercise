import pandas as pd

crime = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv')

crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime = crime.set_index('Year', drop=True)
crime = crime.drop('Total', axis=1)

crime_by_decade = crime.resample('10AS').sum()
crime_by_decade.Population = crime.resample('10AS').max()

#dangerous year
print(crime_by_decade.idxmax())