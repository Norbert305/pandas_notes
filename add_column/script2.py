

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

# Add columns here

df['Is taxed?'] = 'Yes' # Notice all of the values of the new column is Yes.

print(df)


# output bellow

# Product ID	    Description	    Cost to Manufacture	Price	Is taxed??
#       1	       3 inch screw	            0.5	        0.75	Yes
# 	    2	       2 inch nail	            0.1	        0.25	Yes
# 	    3	       hammer	                3.0	        5.5	    Yes
#       4	       screwdriver	            2.5	        3.0	    Yes