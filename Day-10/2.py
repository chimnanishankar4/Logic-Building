#2.Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
import numpy as np
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(a))
#print(np.isscalar([3.1]))
