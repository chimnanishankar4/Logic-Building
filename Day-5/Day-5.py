#!/usr/bin/env python
# coding: utf-8

# In[29]:


#1.Write a Python program to sort a list of elements using the bubble sort Algorithm.
def bubble_sort(list1):
    for i in (list1):
        for j in range(len(list1)-1):
            if list1[j]>=list1[j+1]:
                list1[j+1],list1[j]=list1[j],list1[j+1]
    print("Element to be sort using bubble sort:",list1)
bubble_sort([44,33,55,11,22])
    


# In[35]:


#2.Write a Python program for sequential search (Linear search).
def linear_search(list1,item):
    pos=0
    found=False
    while pos < len(list1) and not found:
        if list1[pos]==item:
            found = True
        else:
            pos+=1
    return(found,pos)
linear_search([11,22,33,44,55],55)
linear_search([11,22,33,44,55],33)    


# In[ ]:


#3.Write a Python program for Binary search.
def binary_search(list1,item):
    first=0
    last=len(list1)-1
    found=False
    pos1=-1
    while (first<=last and not found):
        mid=(first+last)//2
        pos=mid
        if list1[mid]==item:
            found = True
            return (found,pos)
        else:
            if item < list1[mid]:
                last=mid - 1
                
            else:
                first=mid + 1
               
    return (found,pos1)
       
num=binary_search([11,22,33,44,55,66],66)
print(num)

num=binary_search([11,22,33,44,55,66],77)
print(num)


# In[ ]:


'''

4.Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]

'''
list1 = ["M","na","i","lak"]
list2 = ["y","me","s","han"]

print("First original list:",list1)
print("Second original list:",list2)

res=[i + j for i,j in zip(list1,list2)]
print("Concatenate two list:",res)


# In[ ]:


'''
5.	Iterate a given list and check if a given element already exists in a dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
'''
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {"John":47,"Peter":64,"Mahi":37,"Maria":76}
list1=[]
for i in roll_number:
    if i in sampledict.values():
        list1.append(i)
print(list1)
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




