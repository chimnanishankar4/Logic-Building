'''
2.From a list containing ints, strings and
floats, make three lists to store them separately.
'''
list1=[2,'a','b',23.22,4,'c',14.34,6,12.20]
listint=[i for i in list1 if isinstance(i,int)]
print("Integer values:",listint)
liststr=[i for i in list1 if isinstance(i,str)]
print("String values:",liststr)
listfloat=[i for i in list1 if isinstance(i,float)]
print("Floating values:",listfloat)
