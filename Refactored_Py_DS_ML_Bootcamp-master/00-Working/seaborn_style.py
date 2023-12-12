import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# You can use this to set particular styles for the plots
# There are lots of preset themes you can use, or you can create your own
# Check out the documentation for more info on this (https://seaborn.pydata.org/tutorial/aesthetics.html)
sns.set_style("whitegrid")
# despine will remove the lines on the right and top of the plot
# if you want you can specify which sides to remove, below removes all sides
sns.despine(left=True, bottom=True)
# You can also set the size of the figure
plt.figure(figsize=(12, 3))
# The set_context is used to override the default parameters of the plots to match the use case
sns.set_context("poster", font_scale=1)


# example plot
sns.countplot(x="sex", data=tips)

# You can also use matplotlib to change the pallette
# Lots of options for this, check out the documentation for more info on this (https://matplotlib.org/examples/color/colormaps_reference.html)
sns.lineplot(x="total_bill", y="tip", data=tips, palette="rainbow")
