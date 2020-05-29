#3.Write a program to implement multiple inheritance.
#2 way solution 
'''
#1st solution
class P1:
    def m1(self):
        print("P1 method")

class P2:
    def m1(self):
        print("P2 method")
class C(P1,P2):
    pass

c=C()
c.m1()

'''
#2nd solution
class P1:
    def m1(self):
        print("P1 method")

class P2:
    def m1(self):
        print("P2 method")
class C(P2,P1):
    pass

c=C()
c.m1()
