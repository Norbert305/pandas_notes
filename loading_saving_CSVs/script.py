import codecademylib3
import pandas as pd


# When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():

df = pd.read_csv('sample.csv') # pass as an argument to load spreadsheet into the data frame

df.to_csv('sample.csv') # can pass as an argument to save to your current directory


print(df) # run your code to see the data.