import numpy as np
import pandas as pd
import regular_expressions as re

labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {"a": 10, "b": 20, "c": 30}

# Series
# These will create a labelled series for the data passed in
# These act as a kind of hybrid between a list and a dictionary
print(pd.Series(data=my_data))
# You also do not have to specify labels/data, as long as you pass in the data first
print(pd.Series(my_data, labels))

# You can also pass in a dictionary, and the keys will be the labels
pd.Series(d)

# You can also pass in built in functions and have the Series call them
pd.Series(data=[sum, print, len])

ser1 = pd.Series(data=[1, 2, 3, 4], index=["USA", "Germany", "USSR", "Japan"])
print(ser1)
ser2 = pd.Series(data=[1, 2, 5, 4], index=["USA", "Germany", "Italy", "Japan"])
print(ser2)

# You can parse the data by using the index the same you would a dictionary
print(ser1["USA"])

# You can also add series together, and it will add the values together based on the index
# If there is no index match, it will return NaN
print(ser1 + ser2)
