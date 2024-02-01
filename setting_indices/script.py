import codecademylib3
import pandas as pd

# When we select a subset of a DataFrame using logic, we end up with non-consecutive indices. This is inelegant and makes it hard to use .iloc().

# We can fix this using the method .reset_index().



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


# select feb, apr, & june based on the index of the rows
df2 = df.loc[[1, 3, 5]]

# looks like you use the reset method to reset the index of the rows
df3 = df2.reset_index()

df2.reset_index(inplace = True, drop = True)

print(df2)


