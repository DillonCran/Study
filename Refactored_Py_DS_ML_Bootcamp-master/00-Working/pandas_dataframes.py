import numpy as np
import pandas as pd

# imports randn func directly
from numpy.random import randn

# imports seed for random numbers
np.random.seed(101)

# this creates a dataframe with 5 rows and 4 columns
# the first arg is the data, the second is the index, and the third is the columns
# This is comprised of several series objects that share the same index
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)

# This is how you index a column
# Indexed columns are series objects
print(df["W"])
# This is how you index multiple columns, pass in a list of column names
df[["W", "Z"]]
# You can also index a column like this
# This is not recommended because it can be confused with methods, is legacy from SQL, and can cause issues
print(df.W)

# creating a new column
# You create the new name, and then pass in the values.
# It will return an error there is no data for the index
df["new"] = df["W"] + df["Y"]

# removing columns
# axis=1 is for columns, axis=0 is for rows
# this does not actually remove the column, it just returns a new dataframe without the column
df.drop("new", axis=1)
# If you want to actually remove the column, you need to set inplace=True
df.drop("new", axis=1, inplace=True)

# This returns a tuple of the shape
df_shape = df.shape

# Selecting rows
# You can select rows by using the loc method
dfAd = df.loc["A"]
# You can also select rows by using the iloc method if you want to use the index number
dfI = df.iloc[2]

# Selecting subsets of rows and columns
# This is how you select a specific value
all_subset = df.loc["B", "Y"]
# for multiple values, you pass in a list of rows and columns
subset = df.loc[["A", "B"], ["W", "Y"]]
# You can also use iloc
subset = df.iloc[[0, 1], [0, 2]]

# Conditional selection
# This returns a boolean dataframe of the values that meet the condition
bool_df = df > 0
print(bool_df)
# You can apply this to the dataframe to return the values that meet the condition
dooled_df = df[bool_df]
print(dooled_df)

# You can also do this in one step
df[df > 0]

# You can also do this with a specific rows where a column meets a condition
# This returns a dataframe where the values in the W column are greater than 0 and not null
df[df["W"] > 0]

# multiple conditions
# Use the & operator for and instead of AND
# Use the | operator for or instead of OR
# by seperating the arguments in brackets it allows for mutliple conditions
sliced_df = df[(df["W"] > 0) & (df["Y"] > 1)]
print(sliced_df)

# Resetting the index
# This will add the index as a seperate column and reset the index to a range
# This is not inplace, so you need to set inplace=True
print(df)
print(df.reset_index())

# Setting a new index
new_index = "CA NY WY OR CO".split()
df["States"] = new_index
print(df)

# You can set the index to a column
# This is not inplace, so you need to set inplace=True
df.set_index("States")
print(df)

# index levels
# This creates a multi-index dataframe
# You can pass in a list of lists to create a multi-index
# This is a dataframe with two levels of index
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
# Below makes a list of tuples
hier_index = list(zip(outside, inside))
# This creates a multi-index from the list of tuples
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ["A", "B"])
print(df)

# slicing a multi-index dataframe is done like this
df.loc["G1"]  # returns all rows with G1
df.loc["G1"].loc[1]  # returns all rows with G1 and 1 as the index
df.loc["G1"].loc[1]["A"]  # returns the value of A for G1 and 1

# naming index levels
# This will set a name header for the index columns
df.index.names = ["Groups", "Num"]
print(df)

# cross section
# This is a way to select a specific row or column from a multi-index dataframe
# This will retrun all rows labeled 1 from the Num index
df.xs(1, level="Num")
