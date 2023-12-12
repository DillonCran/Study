import numpy as np

# Create an array
arr = np.arange(0, 11)
print(arr)

# Get a value at an index
print(arr[8])
# Get values in a range
print(arr[1:5])
# Get values from the beginning to an index
print(arr[:6])
# Get values from an index to the end
print(arr[5:])

# Broadcasting
# Setting a value with index range (Broadcasting)
print(arr)
arr[0:5] = 100
print(arr)

# If you broadcast to a slice of a numpy array, it will broadcast to the original array.
# To make a copy, you need to be explicit.
slice_arr = arr[0:6]
print(slice_arr)
slice_arr[:] = 99
print(slice_arr)
print(arr)

# To make a copy, you need to be explicit.
arr_copy = arr.copy()
print(arr_copy)

# Indexing a 2D array (matrices)
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)

# double bracket format, == arr_2d[row][col]
print(arr_2d[0][0])

# single bracket format, == arr_2d[row, col]
print(arr_2d[0, 0])

# 2D array slicing
# The below code grabs the top right corner of the matrix.(10, 15), (25, 30)
# :2 means grab everything up to row 2, and 1: means grab everything from column 1 onwards.
print(arr_2d[:2, 1:])

# conditional selection
# You can condiitional arguments to create boolean arrays that can be used to filter data.
arr = np.arange(1, 11)
print(arr)
bool_arr = arr > 5
print(bool_arr)
# This is how you cast bool array to the original array.
print(arr[bool_arr])

# You can also do this in one step.
print(arr[arr > 5])
print(arr[arr % 2 == 0])
