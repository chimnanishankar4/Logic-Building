#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1.Write a NumPy program to create a 3X4 array using and iterate over it.
import numpy as np
array_a=np.arange(1,13).reshape(3,4)
print(array_a)
for i in np.nditer(array_a):
    print(i,end=" ")


# In[7]:


#2.Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
import numpy as np
array_a=np.linspace(5,50,10)
print(array_a)


# In[9]:


#3.Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
import numpy as np
a=np.arange(21)
print("Original array",a)
a[(a>=9) & (a<=15)]
print(a)


# In[10]:


#4.Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
import numpy as np
array_a=np.random.randint(0,10,5)
print(array_a)


# In[11]:


#5.Write a NumPy program to multiply the values of two given vectors.
import numpy as np
array_a=np.array([5,5])
array_b=np.array([5,5])
array_c=array_a*array_b
print("Multiply:",array_c)


# In[14]:


#6.Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
import numpy as np
array_a=np.arange(10,22).reshape(3,4)
print(array_a)


# In[17]:


#7.Write a NumPy program to find the number of rows and columns of a given matrix.
import numpy as np
array_a=np.arange(10,22).reshape(3,4)
print("The number of rows and columns ",np.shape(array_a))


# In[18]:


#8.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
import numpy as np
array_a=np.eye(3)
print(array_a)


# In[24]:


#9.Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
import numpy as np
array_a=np.ones((10,10))
array_a[1:-1,1:-1]=0
print(array_a)


# In[26]:


#10.Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.
import numpy as np
array_a=np.diag([1,2,3,4,5])
print(array_a)


# In[28]:


#11.Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
import numpy as np
array_a=np.zeros((4,4))
array_a[::2,1:2]=1
array_a[1:2,::2]=1
print(array_a)


# In[29]:


#12.Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
import numpy as np
array_a=np.random.random(3,3,3)
print(array_a)


# In[36]:


#13.Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array. 
import numpy as np
a=np.array([[1,2],[2,3]])
print(np.sum(a))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))


# In[37]:


#14.Write a NumPy program to compute the inner product of two given vectors.
x=np.array([2,3])
y=np.array([2,3])
print(np.dot(x,y))


# In[ ]:




