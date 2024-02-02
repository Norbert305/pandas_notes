

# Let's add a new column to our data frame


import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here to the data frame table

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

print(df) 

# output bellow

# Product ID	    Description	    Cost to Manufacture	Price	Sold in Bulk?
#       1	       3 inch screw	            0.5	        0.75	Yes
# 	    2	       2 inch nail	            0.1	        0.25	Yes
# 	    3	       hammer	                3.0	        5.5	    No
#       4	       screwdriver	            2.5	        3.0	    No



