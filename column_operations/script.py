import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here

df["Lowercase Name"] = df.Name.apply(str.lower)


print(df)

# we are adding a new column and adding the data from name in to it making it lower case.

# output


# 	Name	            Email	            Lowercase Name
# 	JOHN SMITH	john.smith@gmail.com	    john smith
# 	Jane Doe	jdoe@yahoo.com	            jane doe
# 	joe schmo	joeschmo@hotmail.com	      joe schmo