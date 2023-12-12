import numpy as np
import pandas as pd

# Data
data = {
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350],
}

df = pd.DataFrame(data)
print(df)

# You can group columns together with groupby
# After assigning the group to a variable, you can call aggregate functions on it
# If the data in the column does not make sense to be aggregated, it will be ignored
df_company = df.groupby("Company")
print(df_company.mean())
print(df_company.max())
print(df_company.min())
print(df_company.std())
print(df_company.count())
print(df_company.describe())
