"""
Your honour, league of legends.  Death.
"""

import numpy as np

# this is a 1-dimensional array
my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

# This is a matrix
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
exx = np.array(my_mat)
print(exx)

# creating a range using numpy, same as defauly python range
np.arange(0, 10)
np.arange(0, 11, 2)

# You can cast empty arrays/matrixies
# These need to be cast as tuples, not just straight number inputs
np.zeros(3)
np.zeros((5, 5))
np.ones(3)
np.ones((3, 3))

# linspace is similar to arange, but you specify the number of points you want
# below will generate 3 values evenly spaced between 0 and 10
linee = np.linspace(0, 7, 3)
print(linee)

# This creates an identity matrix
# Identity matrix is a square matrix with 1's on the diagonal and 0's everywhere else
# The number passed in is the number of rows and columns
eyes = np.eye(4)
print(eyes)

# This is how you generate random numbers
# rand will generate a uniform distribution between 0 and 1 for the number of values you specify
rand = np.random.rand(5)
print(rand)


# You can also make it generate a matrix instead of an array by passing in the number of rows and columns
randx = np.random.rand(5, 5)
print(randx)

# randn will generate a gaussian distribution (both neg and pos numbers between 0 and 1)
randnx = np.random.randn(2)
print(randnx)

# randint will generate random integers between the two numbers you specify
randint = np.random.randint(1, 100, 10)
print(randint)

# You can also reshape arrays and matrices
# If the array you are shaping does not have enough values to fill the new matrix, it will throw an error
arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)

reshaped = arr.reshape(5, 5)
print(reshaped)

# how to find the max value of an array
ranarr_min = ranarr.min()
ranarr_max = ranarr.max()
print(ranarr_max)
print(ranarr_min)

# find the shape of a vector with shape
# this will return a tuple with the first value being the number of items in a row, and the second being the number of rows
print(arr.shape)
print(reshaped.shape)

# find the data type of an array
arr_type = arr.dtype
print(arr_type)

# If you want tto import the numpy library functions, you can do it like this
from numpy.random import randint

randint(2, 10)  # instead of np.random.randint(2, 10)
