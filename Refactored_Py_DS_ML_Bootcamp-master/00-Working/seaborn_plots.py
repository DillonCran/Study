import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())

# displot
# creates a histogram with a KDE (Kernel Density Estimation) line
# KDE = Kernel Density Estimation
# bins = number of bars
displat = sns.displot(tips["total_bill"], kde=False, bins=30)

# jointplot
# creates a plot of two variables with bivariate and univariate graphs
# You can use kind to change the type of graph (scatter, reg, resid, kde, hex)
joint = sns.jointplot(x="total bill", y="tip", data=tips, kind="scatter")

# pairplot
# creates a plot of all numerical columns in a dataframe
# If the two variables are the same, it will create a histogram of that variable
# you can use hue to add a categorical variable to the plot for easy visualisation
# palette changes the colour of the hue
pairpl = sns.pairplot(tips, hue="sex", palette="coolwarm")

# rugplot
# This only plots ticks where a value is present
rugplot = sns.rugplot(tips["total_bill"])

# kdeplot
# This plots a kernel density estimation on the rugplot
# This is done my measuring gaussian distributions at each tick mark and then adding them together to get a smooth curve
kdeplot = sns.kdeplot(tips["total_bill"])
