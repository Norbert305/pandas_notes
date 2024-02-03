

import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

# let's find all of the max prices for each shoe
pricey_shoes = orders.groupby('shoe_type').price.max()

print(pricey_shoes)

print(type(pricey_shoes))


# shoe_type	            price
# ballet flats	        498
# sandals	            498
# stilettos	            468
# wedges	            488



# let's reset our index of pricey_shoes

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()

print(pricey_shoes)

print(type(pricey_shoes))