import pandas as pd

chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')
name_price = chipo[['item_name', 'item_price']]
name_price_sorted = name_price.sort_values('item_name')
chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype('float')

most_exp_quantity = chipo.sort_values('item_price').tail(1)['quantity'].values

veggie_orders = chipo[chipo.item_name == "Veggie Salad Bowl"]
canned_soda_mt_1 = len(chipo.query('quantity > 1 & item_name == "Canned Soda"'))
canned_soda_mt_1 = len(chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)])