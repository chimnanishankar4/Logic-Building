#6.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np
array_a=([11,22,33,44,55,66,77])
array_b=([22,33,44,55,11,66,77])
print("greater",np.greater(array_a,array_b))
print("greater_equal",np.greater_equal(array_a,array_b))
print("less",np.less(array_a,array_b))
print("less_equal",np.less_equal(array_a,array_b))

