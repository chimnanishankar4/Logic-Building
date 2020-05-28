#2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2*3.14
    def perimeter(self):
        return 2*3.14*self.r
c=Circle(10)
print("The area of circle:",c.area())
print("The area of perimeter:",format(c.perimeter(),".2f"))
