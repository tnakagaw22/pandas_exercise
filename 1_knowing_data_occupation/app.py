import pandas as pd

users = pd.read_csv('1_knowing_data_occupation/data.txt', sep='|')
users = users.set_index('user_id', drop=True)

# users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',
#                       sep='|', index_col='user_id')

types = users.dtypes
occu_count = users['occupation'].value_counts().count()
occu_uniq = users.occupation.nunique()
most_freq = users['occupation'].value_counts().sort_values(ascending=False).head(1)

users.describe(include='all')
least_freq_age = users.age.value_counts().tail()

