#4. Write a program to count how many reference variables in a program. 

import sys
class Demo:
    pass
d1=Demo()
d2=d1
d3=d2
d4=d3
print("The number of reference variables:",sys.getrefcount(d1))
