import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([7, 8, 9, 10, 11, 12])

# so here we can perform any mathmetical operation on array.

print(arr1-arr2)

# this is called vector multiplication
print(arr1 * arr2)

# this is called scalar multiplication
print(arr1 * 2)

print(arr1 / arr2)

# whereever in the arr1 the condition satisfies, it will return true otherwise false
print(arr1 > 3)


arr3 = np.arange(6).reshape(2, 3)
arr4 = np.arange(6, 12).reshape(3, 2)

# dot multiplicati or matrix multiplication
print(arr1.dot(arr2)) 

print(arr4.max())

print(arr4.min())

# give the minimum value in each column, axis = 0 means column wise operation, axis = 1 means row wise operation
print(arr4.min(axis=0))
print(arr4.max(axis=1))

print(arr4.sum())
print(arr4.sum(axis=0))

print(arr4.mean(axis=1))

print(arr4.std())

print(np.sin(arr4))
print(np.median(arr4))
