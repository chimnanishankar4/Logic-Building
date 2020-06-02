#4.Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np
array_a=np.array([0,0,0,0,0])
print("Original Array:",array_a)
print(np.any(array_a))
array_b=np.array([1,2,0,0,0])
print("Original Array:",array_b)
print(np.any(array_b))

