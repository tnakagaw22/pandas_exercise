import pandas as pd

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')

avg_beer_by_continent = drinks[['beer_servings', 'continent']].groupby('continent').mean().sort_values('beer_servings', ascending=False)
wine_by_continent_stats = drinks[['wine_servings', 'continent']].groupby('continent').describe()
mean_by_continent = drinks.groupby('continent').mean()
mean_by_continent = drinks.groupby('continent').median()
spirit_stats = drinks[['spirit_servings', 'wine_servings']].agg(['mean', 'min', 'max'])