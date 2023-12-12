import numpy as np
import pandas as pd

d = {"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]}
df = pd.DataFrame(d)

# By default, dataframes will display nan values
print(df)

# to drop nan values, you can use the dropna method
# This will drop any row with a nan value
df.dropna()
# to drop columns, you can pass in axis=1
df.dropna(axis=1)

# You can set a threshold for how many nan values are allowed
# This will drop any row with 2 or more nan values
df.dropna(thresh=2)

# You can also fill in nan values
# This will fill in nan values with the mean of the column
df["A"].fillna(value=df["A"].mean())
# You can fill with anything
df.fillna(value="FILL VALUE")
