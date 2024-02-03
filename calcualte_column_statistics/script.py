import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')


# find the median in our list
# print(customers.age)
# >> [23, 25, 31, 35, 35, 46, 62]
# print(customers.age.median())
# >> 35



# find how many shipments went to the same state
# print(shipments.state)
# >> ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
# print(shipments.state.nunique())
# >> 3

print(orders.head(10))


most_expensive = orders.price.max() # find the most expensive value in the price column

num_colors = orders.shoe_color.nunique() # find the total number of different colors, of shoes we are selling

print(most_expensive) # 493.0

print(num_colors) # 5



# 	id	first_name	last_name	    email	            shoe_type	shoe_material	shoe_color	price
# 0	41874	Kyle	Peck	    KylePeck71@gmail.com	ballet flats	faux-leather	black	385.0
# 1	31349	Elizabeth	Velazquez	EVelazquez1971@gmail.com	boots	fabric	    brown	388.0
# 2	43416	Keith	Saunders	    KS4047@gmail.com	sandals	        leather	         navy	346.0
# 3	56054	Ryan	Sweeney	    RyanSweeney14@outlook.com	sandals	    fabric	      brown	    344.0
# 4	77402	Donna	Blankenship	DB3807@gmail.com	stilettos	fabric	            brown	289.0
# 5	97148	Albert	Dillon	Albert.Dillon@gmail.com	wedges	fabric	                brown	266.0
# 6	19998	Judith	Hewitt	JudithHewitt98@gmail.com	stilettos	leather	        black	395.0
# 7	83290	Kayla	Hardin	Kayla.Hardin@gmail.com	    stilettos	leather	        white	241.0
# 8	77867	Steven	Blankenship	Steven.Blankenship@gmail.com	wedges	leather	     navy	266.0
# 9	54885	Carol	Mclaughlin	CM3415@gmail.com	ballet flats	faux-leather	brown	440.0