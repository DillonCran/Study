import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tips = sns.load_dataset("tips")

# Regression Plots
# You can call normal matplotlib functions to modify the resulting plot
# markers can be found at https://matplotlib.org/api/markers_api.html
# scatter_kws are passed to the scatter layer of the matplotlib call, changing the size and color of the points
# (s is size, c is color, etc.) must be a dictionary.
regg = sns.Implot(
    x="total_bill",
    y="tip",
    data=tips,
    hue="sex",
    markers=["o", "v"],
    scatter_kws={"s": 100},
)
plt.show()

# You can also call a seperate column instead of using hue for col and row arguments
# hue can be placed on top of this as well
# aspect and size are used to change the size of the plots
regg = sns.Implot(
    x="total_bill",
    y="tip",
    data=tips,
    col="sex",
    row="time",
    hue="smoker",
    aspect=0.6,
    size=8,
)
plt.show()
