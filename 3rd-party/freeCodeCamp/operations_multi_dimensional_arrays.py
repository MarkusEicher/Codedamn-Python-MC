import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)
subarr = arr[0:2, 1:3]
print(subarr)

# Modify the subarray by multiplying it by 2
subarr *= 2

# Access an element at row 1, column 2
# print(arr[1, 2])  # Output: 7

# Modify an element at row 0, column 3
# arr[0, 3] = 20

# Print the modified array
print(arr)