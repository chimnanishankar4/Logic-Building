#4.Write a program to implement operator overloading in python.
class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("The addition of:",self.a+self.b)

a=Addition(10,20)
a.add()
a1=Addition("shankar","Chimnani")
a1.add()
