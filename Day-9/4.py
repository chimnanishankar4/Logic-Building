#4.Write a python program to check given car registration number is valid Maharashtra state registration number or not?
import re
s=input("Enter your email address:")
m=re.fullmatch("MH[0-9]{2}[A-Z]{2}\d{4}",s)
if m!=None:
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")
