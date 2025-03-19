from kagglehub import dataset_download
from sqlite3 import connect
from pandas import read_sql_query

path = dataset_download("snap/amazon-fine-food-reviews")
print("Path to dataset files:", path)
conn = connect(path+'/database.sqlite')

df = read_sql_query(""" SELECT * FROM Reviews""", conn)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df = df[['UserId', 'ProductId', 'Score']]
df.columns = ['user_id', 'item_id', 'rating']

df['user_id'] = df['user_id'].astype('category').cat.codes
df['item_id'] = df['item_id'].astype('category').cat.codes
df['rating'] = df['rating'].astype(float)

# Keep users with at least 50 reviews
min_reviews = 50
user_counts = df['user_id'].value_counts()
df = df[df['user_id'].isin(user_counts[user_counts >= min_reviews].index)]

# Keep products with at least 5 reviews
# item_counts = df['item_id'].value_counts()
# df = df[df['item_id'].isin(item_counts[item_counts >= min_reviews].index)]

df.to_csv("../data/reviews.csv", index=False)