#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1: From given data set print first and last five rows
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data.csv")
print("First 5 records")
print(df.head())
print("Last 5 records")
print(df.tail())


# In[5]:


#Question 2: Clean data and update the CSV file.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data.csv",na_values=({
    'price':("?","n.a"),
    'company':("?","n.a"),
    'body-style':("?","n.a"),
    'wheel-base':("?","n.a"),
    'length':("?","n.a"),
    'engine-type':("?","n.a"),
    'num-of-cylinders':("?","n.a"),
    'horsepower':("?","n.a"),
    'average-mileage':("?","n.a"),
    'price':("?","n.a")}))

print(df)
df=df.to_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data2.csv")
    


# In[6]:


#Question 3: Find the most expensive car company name.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data1.csv")
df[['company','price']][df.price==df['price'].max()]


# In[7]:


#Question 4: Print All Toyota Cars details.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data1.csv")
df1=df.groupby('company')
df=df1.get_group('toyota')
df


# In[8]:


#Question 5: Count total cars per company.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data1.csv")
df['company'].value_counts()


# In[9]:


#Question 6: Find each company’s Higesht price car.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data1.csv")
df1= df.groupby('company')
df = df1['company','price'].max()
df


# In[10]:


#Question 7: Find the average mileage of each car making company.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data1.csv")
df1= df.groupby('company')
df = df1['company','average-mileage'].max()
df


# In[12]:


#Question 8: Sort all cars by Price column.
import pandas as pd
df=pd.read_csv("F:\\DBDA-VITA\\python\\CSV files\\Automobile_data1.csv")
df = df.sort_values(by=['price',], ascending=False)
df.head(5)


# In[14]:


#Question 9: Concatenate two data frames using the following conditions
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
df1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
df2 = pd.DataFrame.from_dict(japaneseCars)
carsDf = pd.concat([df1, df2], keys=["Germany", "Japan"])
carsDf


# In[16]:


#Question 10: Merge two data frames using the following condition
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
df1 = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
df2 = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(df1, df2, on="Company")
carsDf


# In[ ]:




