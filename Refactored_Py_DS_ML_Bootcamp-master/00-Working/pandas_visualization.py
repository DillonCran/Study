import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# While pandas CAN plot directly off a dataframe, it's better to use matplotlib or seaborn
# Seaborn will apply style to plots and make it look better even if you're using plt/pd


# Iporting data from CSV
df1 = pd.read_csv(
    "D:\\Projects\\Refactored_Py_DS_ML_Bootcamp-master\\07-Pandas-Built-in-Data-Viz\\df1",
    index_col=0,
)
df2 = pd.read_csv(
    "D:\\Projects\\Refactored_Py_DS_ML_Bootcamp-master\\07-Pandas-Built-in-Data-Viz\\df2"
)
df3 = pd.read_csv(
    "D:\\Projects\\Refactored_Py_DS_ML_Bootcamp-master\\07-Pandas-Built-in-Data-Viz\\df3"
)

print(df1.head())

df1["A"].hist(bin=30)

# Plotting a column
# You can specify what kind of plot you want to use with the kind parameter
df1["A"].plot(kind="hist", bins=30)
df1["A"].plot.hist()


# area plot
df2.plot.area(alpha=0.5)
plt.show()

# bar plot
# stacked =true will stack the bars on top of each other instead of beside
df2.plot.bar(stacked=True)
plt.show()

# histogram
df1["A"].plot.hist(bins=50)
plt.show()

# line plot
# figsize is a tuple of width and height in inches
# lw is line width
df1.plot.line(x=df1.index, y="B", figsize=(12, 3), lw=1)
plt.show()

# scatter plot
# You can pass in a column name to color the points by that column value (c=)
# This is useful for seeing if there is a correlation between two columns
# cmap is a colormap
df1.plot.scatter(x="A", x="B", c="C", cmap="coolwarm")
# You can show the corrilation by using size instead of colour (s=)
# If the point sizes are too small, you can multiply the column by a number to make them bigger
df1.plot.scatter(x="A", x="B", s=df1["C"] * 100)

# box plot
df2.plot.box()
plt.show()
