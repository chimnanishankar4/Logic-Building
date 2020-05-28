#5. write any program to achieve composition in Python
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car Name:",self.name)
        print("Car model:",self.model)
        print("Car color:",self.color)

class Employee:
    def __init__(self,eno,ename,car):
        self.eno=eno
        self.ename=ename
        self.Car=car

    def empinfo(self):
        print("Employee number:",self.eno)
        print("Employee Name:",self.ename)
        print("Car information....")
        self.Car.getinfo()
car=Car("Innova","2.5","Gray")
emp=Employee(101,"Shankar",car)
emp.empinfo()
