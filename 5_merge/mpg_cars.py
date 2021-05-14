import pandas as pd
import numpy as np

cars1 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv')
cars2 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv')

cars1 = cars1.loc[:, 'mpg':'car']
# cars = cars1.set_index('car').join(cars2.set_index('car'), lsuffix='_left', rsuffix='_right')
# cars = cars1.merge(cars2, on='car')
cars = cars1.append(cars2)

# owners = pd.Series(range(15000, 15000 + len(cars)))
owners = np.random.randint(15000, high=73001, size=len(cars), dtype='l')
cars['owners'] = owners