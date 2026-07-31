# nupmy array are faster then the list.
# if list and array both storing the same number of element then the array uses less memory in comparison to the list.
#

# List vs Arrays
# Faster
# Convinent
# Less Memory

import numpy as np

import sys
# sys means system, it has a method name getsizeof

import time
# we will use this to calculate the list is faster or array

list1 = range(100)
print(list1)

arr1 = np.arange(100)
print(arr1)

# calculating size of list
print(sys.getsizeof(87)*len(list1))

#calculating the size of numpy array
print(arr1.itemsize*arr1.size)

x = range(10000000)
y = range(10000000, 20000000)

start_time = time.time()

c = [(x,y) for x,y in zip(x,y)]

print(time.time() - start_time)

a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start_time = time.time()
c = a+b

print(time.time() - start_time)





