#8.Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
import numpy as np
array_a=np.array([1,7,13,105])
print("Original array:",array_a)
print("%d bytes:"%(array_a.size*array_a.itemsize))
