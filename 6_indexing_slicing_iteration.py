#rshape

import numpy as np

arr1 = np.arange(24)
print(arr1)

arr1 = arr1.reshape(6, 4)
print(arr1)

# slicing

# to extract element from 2d array
# arr1[row start: row end, column start: column end]

# to get 2nd row to 3rd row
print(arr1[2:4])

# to get 2nd row (0 based indexing)
print(arr1[2])

# to get first 2 rows
print(arr1[:2])

# to get the 2nd column (0 based indexing), to print a full column we need to print all the rows.
print(arr1[:, 2])

# to get 2nd column to 3rd column like [[element1, element2], [element3, element4], ...]
print(arr1[:, 1:3])

print(arr1[2:4, 1:3])  # from 2nd row to 3rd row and 1st column to 2nd column

print(arr1[4:5, 2:4])

#iteration, row by row
arr2 = np.arange(12)
for i in arr1:
    print(i)

# to get each element one after another even inside
for i in np.nditer(arr1):
    print(i)


