#1.Write a program to implement Constructor with Variable Number of Arguments.
class Test:
    def __init__(self,*args):
        print("sum of numbers:",sum(args))
t1=Test(1)
t2=Test(1,2)
t3=Test(1,2,3)
t4=Test(1,2,3,4)
t5=Test(1,2,3,4,5)
