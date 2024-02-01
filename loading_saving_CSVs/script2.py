import codecademylib3
import pandas as pd
#load the CSV below:

df = pd.read_csv('imdb.csv') # load the csv

print(df.head()) # gives the first 5 rows of the data frame

print(df.info()) # gives some statistics for each column.
