#3.Write python program to check  that given email address is valid or not?
import re
s=input("Enter your email address:")
m=re.fullmatch("\w[_.]*@gmail[.]com",s)
if s!=None:
    print("Valid email address")
else:
    print("Invalid email address")
