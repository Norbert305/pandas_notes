import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)


# let's merge these 2 tables and rename the column called id from the products table to customer_id
orders_products = pd.merge(
    orders,
    products.rename(columns={'id': 'customer_id'}))

# the reason is because the 2nd table doesn't have a customer_id like the first table (product_id). So we merge both tables and rename the column from the 2nd table (id) to product_id
print(orders_products)


# printed tables bellow



# 	id	product_id	customer_id	quantity	timestamp
# 0	1	    3	        2	        1	    2017-01-01
# 1	2	    2	        2	        3	    2017-01-01


#   id	    description	            price
# 0	1	    thing-a-ma-jig	        5
# 1	2	    whatcha-ma-call-it	    10


# 	id	product_id	customer_id	quantity	timestamp	    description	price
# 0	1	    3	        2	        1	    2017-01-01	    whatcha-ma-call-it	10
# 1	2	    2	        2	        3	    2017-01-01	    whatcha-ma-call-it	10
# 2	3	    1	        3	        1	    2017-01-01	    doo-hickey	7


