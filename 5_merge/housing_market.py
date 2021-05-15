import pandas as pd
import numpy as np

series_1 = pd.Series(np.random.randint(1, high=5, size=100))
series_2 = pd.Series(np.random.randint(1, high=4, size=100))
series_3 = pd.Series(np.random.randint(10000, high=30001, size=100))

housemkt = pd.concat([series_1, series_2, series_3], axis=1)

frame = {
    'series_1': series_1,
    'series_2': series_2,
    'series_3': series_3
}
data = pd.DataFrame(frame)
data.rename(columns={'series_1': 'bedrs', 'series_2': 'bathrs', 'series_3': 'price_sqr_meter'}, inplace=True)

bigcolumn = pd.concat([series_1, series_2, series_3])
bigcolumn = bigcolumn.reset_index()
