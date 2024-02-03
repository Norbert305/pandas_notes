
import pandas as pd

# use inventory.csv as our data frame

inventory = pd.read_csv("inventory.csv") # load the inventory from the csv file


staten_island = inventory.head(10) # let's save these rows as a variable

product_request = staten_island.product_description # get us everything from the product_description column


seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")] # retrieve the row for Brooklyn and seeds sold


inventory["in_stock"] = inventory.apply(lambda row : True if row.quantity > 0 else False, axis = 1) # lets add a column to our inventory called in_stock and make the values true unless the quantity is > 0.


inventory["total_value"] = inventory.apply(lambda row: row.price * row.quantity, axis = 1) # create a new column with the key-value data showing the price times the quantity of each item 


# lets combine the values of both the columns product_type and product_description into the combined_lambda variable
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
    
inventory["full_description"] = inventory.apply(combine_lambda, axis = 1) # now lets create a new column called full_description and apply the combine_lambda variable as the values


print(inventory.head(10)) # print the first 10 rows of our data