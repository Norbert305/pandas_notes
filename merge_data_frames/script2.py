import codecademylib3
import pandas as pd

# let's assign our data frame to the variable sales
sales = pd.read_csv('sales.csv')
print(sales) # analyze sales

# let's assign our data frame to the variable targets
targets = pd.read_csv('targets.csv')
print(targets) # analyze targets

# let's assign our third data frame to the variable men_women
men_women = pd.read_csv('men_women_sales.csv')

print(men_women) # anaalyze men_women


# let's merge all 3 data frames into the variable all_data
all_data = sales.merge(targets)\
	.merge(men_women)

# analyze all_data
print(all_data)

# find the rows of the revenue > target and the women > men
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men) ]