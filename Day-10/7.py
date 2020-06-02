#7.Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
import numpy as np
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("Equal:",np.equal(x,y))
print("Equal with tolerance:",np.allclose(x,y))
