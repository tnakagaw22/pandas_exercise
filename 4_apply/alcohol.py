import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv')

# sub_df = df.iloc[:, df.columns.get_loc('school'):df.columns.get_loc('guardian') + 1]
sub_df = df.loc[:, "school":"guardian"]

capitalize = lambda x: x.capitalize()

sub_df['Mjob'] = sub_df['Mjob'].apply(capitalize)
sub_df['Fjob'] = sub_df['Fjob'].apply(capitalize)

# print(sub_df.iloc[len(sub_df) - 1: len(sub_df), :])
print(sub_df.tail(1))

majority = lambda x: x >= 17

sub_df['legal_drinker'] = sub_df['age'].apply(majority)

numberic_columns = sub_df.select_dtypes(include=np.number).columns
sub_df[numberic_columns] = sub_df[numberic_columns].apply(lambda x: x * 10)

def times10(x):
    if type(x) is int:
        return 10 * x
    else:
        return x

sub_df = sub_df.applymap(times10)