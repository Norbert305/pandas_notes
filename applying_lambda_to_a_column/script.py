import codecademylib3
import pandas as pd


#-----------------------------------------------
def last_name(x):
    
    return x.split()[-1]



print(last_name("Bob Marley")) # Marley

#----------------------------------------------




df = pd.read_csv('employees.csv')





# Add columns here
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name) # added the new column last_name and apply the data to it 

print(df)

# output

	# id	    name	          hourly_wage	    hours_worked	    last_name
	# 10310	    Lauren Durham	    19	                 43	            Durham
	# 18656	    Grace Sellers	    17	                 40	            Sellers
	# 61254	    Shirley Rasmussen	16	                 30	            Rasmussen