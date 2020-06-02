#5.Write a NumPy program to test element-wise for NaN of a given array.
import numpy as np
array_a=np.array([4,5,6,7,np.NaN])
print("Original array:",array_a)
print(np.isnan(array_a))
