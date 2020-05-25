#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Write a function to find max of three numbers.
def max_number(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("N1 is greater:",n1)
    elif n2 > n1 and n2 > n3:
        print("N2 is greater:",n2)
    else:
        print("N3 is greater:",n3)
(max_number(11,22,33))


# In[6]:


#2.Write a Python program to detect the number of local variables declared in a function.
def count_localvar():
    x=10
    y=20
    z=30
print("The number of local variables:",count_localvar.__code__.co_nlocals)


# In[11]:


#3.Write a recursive function to calculate the sum of numbers from 0 to 10
#Expected output: 55
def sum_number(n):
    if n<=1:
        return n
    else:
        return n + sum_number(n-1)
   
print("The sum of number using recursion:",sum_number(10))


# In[55]:


#4.Create a function showStudent() in such a way that it should accept student id, name, and it’s college name  and 
#if the id and college name is missing in function call it should show it as by default id is 1 and college name is VITA.
def student_info(name,id=1,clg_name="VITA"):
    print("id:",id,"\nname:",name,"\nclg-Name:",clg_name)
student_info("shankar",101,"Miet")
print()
student_info("shankar")


# In[31]:


'''
5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]
'''
def unique_numbers(list1):
    unique_set=set(list(list1))
    unique_list=list(unique_set)
    print(unique_list)
print("Unique list:")
unique_numbers([11,22,22,33,33,33,44,55,55,66])


# In[58]:


'''
6.	Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
1st for first digit
2nd for last digit
Example:
 Input:  5424
Output: 9
'''
def first_digit(a):
    while a>=10 and a>=1:
        a //=10
    return a
def last_digit(a):
    return a%10
a=int(input("Enter number:"))
print("The first and last digit sum is:",first_digit(a)+last_digit(a))


# In[ ]:





# In[ ]:




