import numpy as np

arr1 = np.arange(12).reshape(3, 4)
print(arr1)

arr2 = np.arange(12, 24).reshape(3, 4)
print(arr2)

print(arr1 + arr2) # this will add the corresponding element of arr1 and arr2 and return a new array

arr3 = np.array([1, 2, 3, 4])

# here the shape of arr1 and arr3, are different but still we can perform the addition operation, this is called broadcasting. so what happens is that the smaller array (arr3) is broadcasted to the shape of the larger array (arr1) and then the operation is performed.
print(arr1 + arr3)


# other useful functions that make your life easier


# np.random.seed(1) # this is used to get the same random numbers every time you run the code, it is used for reproducibility
print(np.random.random(1))

print(np.random.uniform(3, 100)) # this will generate a random number between 3 and 10

print(np.random.uniform(3, 100, 10).reshape(1, 10)) # this will generate a random number between 3 and 10 and reshape it to 2 rows and 5 columns

print(np.random.randint(1, 10)) # this will generate a random integer between 1 and 10 and reshape it to 2 rows and 5 columns

a = np.random.randint(1, 10, 10)
print(a)

print(np.max(a)) # this will return the maximum value in the array

np.argmax(a) # this will return the index of the maximum value in the array. you can use argmin

print(a[np.argmax(a)]) # this will return the maximum value in the array using the index of the maximum value

# replace the odd values with the -1 in the array a
a[a%2 != 0] = -1
print(a)

# where the condition is satisfied it will return true otherwise false, this is called boolean indexing. where(condition, value if true, value if false)

np.where(a%2 == 1, -1, a)

arr4 = np.random.randint(1, 50, 10)
print(arr4)

print(np.sort(arr4))

print(np.percentile(arr4, 99.4)) # this will return the 25th percentile of the array