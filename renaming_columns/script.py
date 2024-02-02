import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

print(df)

# change the old columns into the new columns

# Old	            New
# id	            ID
# name	            Title
# genre	            Category
# year	            Year Released
# rating	        Rating


# another way

# practice = practice.rename(column={
#     'id' : 'Name',
#     'number' : 'age',
#     'time' : 'date'
# })