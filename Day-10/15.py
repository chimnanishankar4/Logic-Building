#15.Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np
array_a=np.arange(15,56)
print("Orignal values:")
print(array_a)

print("Except First and Last value from the array:")
print(array_a[1:-1])
