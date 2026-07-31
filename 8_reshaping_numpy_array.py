import numpy as np
# converting higher function in to 1d array

arr1 = np.arange(6, 12)

print(arr1.ndim)


# change the shape of any dimensional in to 1-d array.
print(arr1.ravel())

arr2 = np.arange(6).reshape(3, 2)
print(arr2.transpose())

arr3 = np.arange(6).reshape(2, 3)
arr5 = np.arange(6, 12).reshape(2, 3)

# combine the 2 array horizontally
print(np.hstack((arr3, arr5)))

# combine the 2 array vertically
print(np.vstack((arr3, arr5)))


