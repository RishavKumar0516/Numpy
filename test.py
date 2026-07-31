import numpy as np

print(np.__version__)



# shape
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1.shape)

print(arr1.ndim)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)

# ndim is used to get the dimension
print(arr2.ndim)

#size is used to now the size
print(arr1.size)

# 
print(arr2.size)
print(arr2.itemsize)
print(arr2.dtype)
print(arr1.dtype)
arr1.astype('float')
print(arr1)