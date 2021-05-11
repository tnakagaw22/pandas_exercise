import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

army = pd.DataFrame(raw_data)
army = army.set_index('origin', drop=True)

veterans = army['veterans']
veterans_death = army[['veterans', 'deaths']]

maine_alaska_data = army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']]
maine_alaska_data_iloc = army.iloc[2:6, 2:5]

army_subset_1 = army.iloc[3:]
army_subset_2 = army.iloc[:, 2:6]
death_mt_50 = army[(army.deaths >= 500) | (army.deaths <= 50)]
regiment_not_Dragoons = army[army.regiment != 'Dragoons']
texas_arizona = army.loc[['Texas', 'Arizona']]
arizona_death = army.iloc[army.index.get_loc('Arizona'), 2]
texas_death = army.iloc[2, army.columns.get_loc('deaths')]
# texas_death = army.loc[:, ['deaths']].iloc[2]