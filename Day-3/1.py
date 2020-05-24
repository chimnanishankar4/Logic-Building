'''
1.You are given with a list of integer elements.
Make a new list which will store square of elements of previous list.
'''
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for i in list1:
    list2.append(i*i)
print("The squares of list elements:",list2)
