import numpy as np

arr1 = np.arange(24).reshape(6, 4)

print(arr1)

# to get the discontinous value row wise
print(arr1[[0, 1]])

# Indeing with boolean values

arr2 = np.random.randint(low = 1, high = 10, size = 20).reshape(4, 5)
print(arr2)

# condition indexing, get 
print(arr2 > 50) # this will return a boolean array, where the condition is satisfied it will return true otherwise false


# indexing using the boolean array
print(arr2[arr2 > 5]) # this will return the value where the condition is satisfied, in this case it will return an empty array because there is no value greater than 50 in arr2

print(arr2[(arr2 > 5) & (arr2%2 !=0)]) # this will return the value where the condition is satisfied, in this case it will return the value greater than 5 and odd number in arr2

arr2[(arr2>5) & (arr2%2 != 0)]=0# this will set the value to 0 where the condition is satisfied, in this case it will set the value to 0 where the value is greater than 5 and odd number in arr2

print(arr2)



