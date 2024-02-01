#Data Frame is an object that stores data as rows and columns like a spreadsheet or sql table.

import codecademylib3
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name' : ['t-shirt', 't-shirt', 'skirt', 'skirt'], 'Color' : ['blue', 'green', 'red', 'black']
})

print(df1) # Data frame prints a table with rows and columns




# Product ID	Product Name	Color
# 0	       1	t-shirt	        blue
# 1	       2	t-shirt	        green
# 2	       3	skirt	        red
# 3	       4	skirt	        black
