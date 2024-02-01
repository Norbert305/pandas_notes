import codecademylib3
import pandas as pd


# Let's load the data from the shoefly.csv file
orders = pd.read_csv('shoefly.csv')

# Let's print the first 5 rows from the csv file
print(orders.head(5))

# print(orders.iloc[:5]) is another way


# select all of the email addresses from the column email and save them to the variable emails
emails = orders.email
print(emails)
# emails = orders['email'] is another way


# Find Francis Palmer's order in the table
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

print(frances_palmer)


# Find the rows listing the data of the confy shoes
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]

print(comfy_shoes)