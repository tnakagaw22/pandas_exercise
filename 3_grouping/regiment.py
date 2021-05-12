import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

regiment = pd.DataFrame(raw_data, columns=raw_data.keys())

nighthawks_preTestScore_mean = regiment.groupby('regiment').mean().loc[['Nighthawks'],['preTestScore']]
stats_by_company = regiment.groupby('company').describe()
preTestScore_mean_by_company = regiment.groupby('company').mean()['preTestScore']
preTestScore_mean_by_regiment_company = regiment.groupby(['regiment', 'company']).preTestScore.mean()
preTestScore_mean_by_regiment_company = regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack()

for name, group in regiment.groupby('regiment'):
    print(name)
    print(group)