import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])


# select the entire first row of january 
january = df[df.month == 'January']



print(january)


# more examples bellow

#     name	      address	            phone	          age
# Martha Jones	123 Main St.	    234-567-8910	       28
# Rose Tyler	456 Maple Ave.	    212-867-5309	       22
# Donna Noble	789 Broadway	      949-123-4567	       35
# Amy Pond	  98 West End Ave.	    646-555-1234	      29
# Clara Oswald	54 Columbus Ave.	714-225-1957	       30



# df[df.age == 30]  --->  Clara Oswald	54 Columbus Ave.	714-225-1957  30

# df[df.age > 30] --->  Donna Noble	789 Broadway	 949-123-4567	 35

# df[df.age < 30] 

# df[df.name != 'Clara Oswald']

