import pandas as pd

baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.drop(columns=['Unnamed: 0'], inplace=True)

# gender_count = baby_names.groupby('Gender')['Gender'].count()
gender_count = baby_names.Gender.value_counts()

# baby_name_grp = baby_names.groupby('Name').sum().sort_values('Count', ascending=False)
names_count = baby_names.groupby('Name').Count.sum().sort_values(ascending=False).head()
unique_names = len(names_count)

most_occur_name = names_count.sort_values(ascending=False).head()

# least_occur_count = names_count.sort_values(ascending=False).tail(1)[0]
least_occur_count = names_count.min()
least_occur_names = names_count[names_count == least_occur_count]

median_name = names_count[names_count == names_count.median()]

names_count.std()
names_count.describe()