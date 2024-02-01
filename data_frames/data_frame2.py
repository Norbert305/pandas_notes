# Same thing as Data_Frame but a different way


import codecademylib3
import pandas as pd


# Our rows created
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
                   
# Our Columns

  columns=[
    #add column names here
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)