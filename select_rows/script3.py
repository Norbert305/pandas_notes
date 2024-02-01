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
           'clinic_west']
)

# print the last 3 rows of the data frame
april_may_june = df.iloc[-3: ]

print(april_may_june)


# id  month	clinic_east	clinic_north	clinic_south	clinic_west
# 3	   April	  80	     80	              54	        180
# 4	   May	    51	         54	             54	            154
# 5	   June	    112	         109	         79	            129