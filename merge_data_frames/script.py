import codecademylib3
import pandas as pd



# let's assign our data frame to the variable sales
sales = pd.read_csv('sales.csv')
print(sales) # analyze the sales

#let's assign our data frame to the variable targets
targets = pd.read_csv('targets.csv')
print(targets) # analyze the targets

# let's merge the 2 data frames of sales and target
sales_vs_targets = pd.merge(sales,targets)

# let's print the merged tables
print(sales_vs_targets)

# let's find the rows with the revenue > target
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

print(crushing_it) # let's print the result here called crushing it






# all_tables = pd.concat([table1, table2])    ---> use this if both tables have the same columns