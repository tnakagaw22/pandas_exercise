import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# set this so the graphs open internally
# %matplotlib inline

chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')

# get the Series of the names
x = chipo.item_name

# use the Counter class from collections to create a dictionary with keys(text) and frequency
letter_counts = Counter(x)

# convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(letter_counts, orient='index')

df = df[0].sort_values(ascending=False).head(5)

# create the plot
df.plot(kind='bar')

# set the title and labels
plt.xlabel('Item')
plt.ylabel('Number of Times Ordered')
plt.title('Most Ordered Chpotle\'s Items')

plt.show()

count_by_order_price = Counter(chipo.item_price)
df_order_price = pd.DataFrame.from_dict(count_by_order_price, orient='index')

# strip the dollar sign and trailing space
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price]
# orders2 = chipo.groupby('order_id').sum()
orders = chipo.groupby('item_name').agg(price=('item_price', 'mean'), quan=('quantity', 'sum'))
x = orders.price
y = orders.quan

plt.scatter(x, y, s=50, c='green')
# df_order_price.plot(kind='scatter')
plt.xlabel('Order Price')
plt.ylabel('Number of Times Ordered')
plt.title('Times Ordered by Order Price')

plt.show()
