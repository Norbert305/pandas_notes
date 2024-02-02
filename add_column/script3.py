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


# adding a new column called sales tax and making the values = price * 0.075
df['Sales Tax'] = df.Price * 0.075

# adding a new column called Margin and subtracting the difference
df['Margin'] = df['Price'] - df['Cost to Manufacture']
# Doing it this way because the column name doesn’t follow our rules for variable names.



print(df)

# output bellow

# Product ID	    Description	    Cost to Manufacture	Price	Sales Tax     Margin
#       1	       3 inch screw	            0.5	        0.75	0.05            0.25
# 	    2	       2 inch nail	            0.1	        0.25	0.018           0.15
# 	    3	       hammer	                3.0	        5.5	    0.4125          2.5
#       4	       screwdriver	            2.5	        3.0	    0.2249          0.5