import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

iris = sns.load_dataset("iris")
print(iris.head())

tips = sns.load_dataset("tips")
print(tips.head())

# Pair Grid
# PairGrid creates a blank array of subplots, and you decide what to plot on each subplot
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()


# Facet Grid
fac = sns.FacetGrid(data=tips, col="time", row="smoker")
fac.map(sns.displot, "total_bill")
plt.show()
