#2.write python program to check  that given number is valid mobile number or not?
import re
s=input("Enter mobile number:")
m=re.fullmatch("[7-9]\d{9}",s)
if m!=None:
    print("Valid mobile number")

else:
    print("Invalid mobile number")
