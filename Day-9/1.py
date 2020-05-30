#1.Write a function to compute divide by zero and use try/except to catch the exceptions.
try:
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    res=x/y
    print("Result:",res)
except Exception as arg:
    print("Exception raised:",arg)
else:
    print("Normal end of the file")
finally:
    print("Finally executed")
