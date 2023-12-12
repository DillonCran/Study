import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4],
        "col2": [444, 555, 666, 444],
        "col3": ["abc", "def", "ghi", "xyz"],
    }
)

print(df.head())


# finding unique values
# This will only return unique values, cutting out the duplicates
print(df["col2"].unique())
# This returns the length of unique values, like len()
print(df["col2"].nunique())
# This returns the number of times each unique value appears
print(df["col2"].value_counts())

# Selecting data
df[df["col2"] > 2]
# You can also use multiple conditions
df[(df["col1"] > 2) & (df["col2"] == 444)]


# Applying functions
def timestwo(x):
    return x * 2


# You can use .apply() to apply a function to series
df["col1"].apply(timestwo)

# You can also use lambda expressions if you want to do something simple
df["col1"].apply(lambda x: x * 2)

# Removing columns
# axis=1 means you're dropping a column, axis=0 means you're dropping a row
# inplace=True means you're actually changing the dataframe, not just returning a copy
df.drop("col1", axis=1, inplace=False)

# Getting column and index names
print(df.columns)
print(df.index)

# Sorting and ordering a dataframe
# You can pass in either a column or row (axis=1) name to sort by
print(df.sort_values("col2"))
print(df.sort_values(by="col2", ascending=False, inplace=False))

# Finding null values
print(df.isnull())

# Pivot tables
ptable = df.pivot_table(values="col3", index=["col1", "col2"], columns="col3")
print(ptable)
