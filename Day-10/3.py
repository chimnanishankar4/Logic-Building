#3.Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
array_a=np.array([1,2,3,0,0])
print("Original array:")
print(array_a)
array_b=np.all(array_a)
print(array_b)
array_c=np.array([1,2,3,4])
print("Original array:")
print(array_c)
array_d=np.all(array_c)
print(array_d)
