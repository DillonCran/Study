import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

# In order to use the heatmap, the data must be in a matrix form
# The index name and column name must match up
# The data must be numerical

# Correlation Matrix
# Remove the non numerical columns
num_tips = tips.select_dtypes(include=np.number)
# map the correlation matrix
tc = num_tips.corr()
# plot the heatmap
# annot = True will show the correlation values
# cmap = 'coolwarm' will show the values in a color gradient
tc_heat = sns.heatmap(tc, annot=True, cmap="coolwarm")
plt.show()

# Pivot Table
flights_pivot = flights.pivot_table(index="month", columns="year", values="passengers")
sns.heatmap(flights_pivot, cmap="magma", linecolor="white", linewidths=1)
plt.show()


# Cluster Map
# Cluster map will cluster the rows and columns together based on their similarities
# standard_scale = 1 will scale the data to have a mean of 0 and a standard deviation of 1
sns.clustermap(flights_pivot, cmap="coolwarm", standard_scale=1)
plt.show()
