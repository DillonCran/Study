import numpy as np

arr = np.arange(0, 11)
print(arr)

# You can do basic arithmetic operations with numpy arrays.
double_arr = arr + arr
print(double_arr)
negative_arr = arr - arr
print(negative_arr)
square_arr = arr * arr
print(square_arr)

# You can also do scalar operations with numpy arrays.
scalar_arr = arr + 100
print(scalar_arr)
scalar_arr = arr - 100
print(scalar_arr)
scalar_arr = arr * 100
print(scalar_arr)
scalar_arr = arr / 100
print(scalar_arr)
scalar_arr = arr**2
print(scalar_arr)

# If you try to divide by zero, you will get a warning, but not an error.
# The result will be nan, which stands for not a number.
# It will still return a result, but it will be a warning.

# You can also do universal array functions.
# These are mathematical operations that you can use to perform the operation across the array.
# sqroot
np.sqrt(arr)
# exponential
np.exp(arr)
# max
# You can also call the max function on the array itself.
np.max(arr)
arr.max()
# You can even do trig functions.
np.sin(arr)
np.log(arr)
np.cos(arr)
# There are a lot of universal array functions.
