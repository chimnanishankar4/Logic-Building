#5.Write a Python program to square and cube every number in a given list of integers using Lambda.
list1=[1,2,3,4,5,6,7,8,9,10]
sq=list(map(lambda n:n*n,list1))
cube=list(map(lambda n:pow(n,3),list1))
print("The squares of list:",sq)
print("The cube of list:",cube)
