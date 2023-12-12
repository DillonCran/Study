import pandas as pd
import numpy as np

# reading CSV files
# You can read form almost any format using pandas .read_ methods
df = pd.read_csv("example")

print(df)

# This is how you save a file
#  input is the name of the file you want to save and index=False means you don't want to save the index as a column
df.to_csv("My_output", index=False)

# Reading and writing excel files
# Pandas can only import data, not formulas or images
exel_df = pd.read_excel("excel_sample.xlsx", sheet_name="Sheet1")
print(exel_df)

# This is how you save an excel file
df.to_excel("Excel_Sample2.xlsx", sheet_name="NewSheet")

# Reading HTML files
# Pandas can read table tabs from HTML files
data = pd.read_html("http://www.fdic.gov/bank/individual/failed/banklist.html")
print(data)

# Reading SQL files
# Pandas is not the best way to read SQL files, but it can be done
# SHOULD be using whatever driver library is designated for the SQL file

# This is how you create the SQL engine
from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:")
# This is how you save the data to the SQL engine
df.to_sql("my_table", engine)
# This is how you read the data from the SQL engine
sqldf = pd.read_sql("my_table", con=engine)
print(sqldf)
