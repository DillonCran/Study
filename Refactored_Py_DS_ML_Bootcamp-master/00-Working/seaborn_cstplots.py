import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
print(tips.head())

# barplot
# x = categorical, y = numerical
# estimator is for the function to aggregate the categorical data
barplot = sns.barplot(x="sex", y="total_bill", data=tips, estimator=np.std)
plt.show()

# countplot
# same as barplot but the estimator is explicitly counting the number of occurrences
countplot = sns.countplot(x="sex", data=tips)
plt.show()

# boxplot
# read the boxplots by looking at the median, the interquartile range, and the whiskers
# hue allows you to use a categorical variable to further divide the data
boxplot = sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")
plt.show()

# violinplot
# similar to boxplot but it shows the distribution of the data
# the white dot is the median
# the thick black bar is the interquartile range
# the thin black line is the 95% confidence interval
# hue can be passed hear to isolate an additional categorical variable, and split can set the violin into halves to compare the distributions
violin = sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.show()

# stripplot
# Scatter plot that is used for categorical data instead of numerical data
# jitter adds random noise to the data to make it easier to read
stripplot = sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# swarmplot
# similar to stripplot but the points are adjusted so that they do not overlap
# combination of stripplot and violinplot
swarmplot = sns.swarmplot(x="day", y="total_bill", data=tips)

# You can combine plots to make more complex plots
# violinplot and swarmplot
violin = sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
swarmplot = sns.swarmplot(
    x="day", y="total_bill", data=tips, color="black", size=3, hue="sex"
)
plt.show()


#  factorplot
# general form of all the plots above
# kind parameter sets the plot type
# col parameter divides the plots by a categorical variable
# row parameter divides the plots by another categorical variable
# hue parameter divides the plots by another categorical variable
# aspect parameter controls the aspect ratio
# size parameter controls the size of the figure
# data parameter is the DataFrame
# palette parameter controls the color of the plot
# col_wrap parameter controls the number of column in the grid
factorplot = sns.factorplot(x="day", y="total_bill", data=tips, kind="bar")
plt.show()
