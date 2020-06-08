#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1.	Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.
import pandas as pd
array=pd.Series([2,4,6,8,10])
print(array)


# In[7]:


#2.Write a Pandas program to convert a Panda module Series to Python list and it’s type.
import pandas as pd
array=pd.Series([2,4,6,8,10])
print("Original series")
print(array)
print(type(array))
print("Convert into list")
print(array.tolist())
print(type(array.tolist()))


# In[8]:


#Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd
a=pd.Series([2,4,6,8,10])
b=pd.Series([2,4,6,8,10])
res=a + b
print("Addition:",res)
res=a - b
print("Substraction:",res)
res=a * b
print("Multiplication:",res)
res=a / b
print("Division:",res)


# In[10]:


#4.Write a Pandas program to compare the elements of the two Pandas Series
import pandas as pd
a=pd.Series([2,4,6,8,10])
b=pd.Series([1,3,5,7,12])
res=a==b
print("Equal:",res)
res=a>b
print("Greater than:",res)
res=a<b
print("Less than:",res)


# In[11]:


#5.Write a Pandas program to convert a dictionary to a Pandas series.Sample dictionary: 
import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original Dict:")
print(d1)
new_series=pd.Series(d1)
print(new_series)


# In[12]:


#6.Write a Pandas program to convert a NumPy array to a Pandas series.
import numpy as np
import pandas as pd
array_a=np.array([2,4,6,8,10])
print("Original array")
print(array_a)
new_series=pd.Series(array_a)
print(new_series)


# In[15]:


#7.Write a Pandas program to change the data type of given a column or a Series.
import pandas as pd
array=pd.Series(['2','4','6','8','10'])
print("Original array")
print(array)
print("Data type is cahnge")
new=pd.to_numeric(array,errors="coerce")
print(new)


# In[18]:


#8.Write a Python Pandas program to convert the first column of a DataFrame as a Series
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
# s1 = df.ix[:,0]
print("\n1st column as a Series:")
# print(s1)
# print(type(s1))


# In[19]:


#9.Write a Pandas program to convert a given Series to an array.
import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Series to an array")
a = np.array(s1.values.tolist())
print (a)


# In[20]:


#10.Write a Pandas program to sort a given Series.
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)


# In[ ]:




