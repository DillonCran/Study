import matplotlib.pyplot as plt

# Use this at the end of the code to show the plot
plt.show()

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

# Functional method
# Pass in the two arrays you wish to plot
# You can also pass in a format string to change the color and line type
plt.plot(x, y, "r-")  # set colour to red
plt.xlabel("X Label")  # label x axis
plt.ylabel("Y Label")  # label y axis
plt.title("Title")  # set title
plt.show()

plt.plot(x, y)
plt.show()

# You can also plot multple plots on the same canvas
plt.subplot(1, 2, 1)  # (rows, columns, plot number)
plt.plot(x, y, "r")  # plot 1
plt.subplot(1, 2, 2)  # (rows, columns, plot number)
plt.plot(y, x, "b")  # plot 2
plt.show()


# Object Oriented method
# Create a figure object and then call methods off of it

fig = plt.figure()  # create figure object
axes = fig.add_axes(
    [0.1, 0.1, 0.8, 0.8]
)  # add axes to figure, left, bottom, width, height
axes.plot(x, y)  # plot on axes
axes.set_xlabel("X Label")  # label x axis
axes.set_ylabel("Y Label")  # label y axis
axes.set_title("OOM Title")  # set title
plt.show()

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes

# subplots in OOM
fig, axes = plt.subplots(nrows=3, ncols=3)  # create 3x3 grid of subplots
axes.plot(x, y)
plt.tight_layout()  # fixes overlapping
plt.show()

# You can also iterate through the axes
for current_ax in axes:
    current_ax.plot(x, y)
plt.show()
# iterate through rows and columns normally

# Figure size and DPI
fig = plt.figure(
    figsize=(3, 2), dpi=100
)  # figsize is a tuple of width and height in inches
# dpi is dots per inch
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)

# Save a figure
# You can save a figure as a png, jpg, svg, pdf, etc.
# You can also specify the dpi
# If you plot multiple plots on the same figure, they will need to be labeled
# You can also specify the location of the legend, with 0 being in the top left corner (default)
# You can also specify the location of the legend with a tuple of coordinates (0,0) being the bottom left corner
fig = plt.figure()
ax = fig.add_axes(0, 0, 1, 1)
ax.plot(x, x**2, label="X Squared")
ax.plot(x, x**3, label="X Cubed")
ax.legend(loc=0)
ax.set_title("saved_fig")
ax.set_xlabel("X")
ax.set_ylabel("Y")
fig.savefig("my_picture.png", dpi=200)


# Plot Appearance
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
# You can use basic str names of colours, RGB codes, or hex codes
# linewidth or lw for short, setting it to 0 will make it disappear, and setting it to 2 will double thickness
# Alpha controls transparency, 0 is transparent, 1 is opaque
# linestyle or ls for short, you can use basic str names or the actual name (dashed, dotted, dashdot,solid, steps, etc.)
# marker is the actual marker on the plot, you can use basic str names or the actual name (o, +, *, 1, 2, 3, etc.)
# markersize or ms for short, sets the size of the marker
ax.plot(
    x,
    y,
    color="orange",
    linewidth=2,
    alpha=0.5,
    linestyle="-.",
    marker="o",
    markersize=10,
    markerfacecolor="yellow",
    markeredgewidth=3,
    markeredgecolor="green",
)


# Control over axis appearance
# You can set the limits of the axis but only data points within the limits will be shown
ax.set_xlim([0, 1])  # set x axis limits
ax.set_ylim([0, 2])  # set y axis limits
plt.show()
