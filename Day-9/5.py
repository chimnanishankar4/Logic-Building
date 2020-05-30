#5.Write a python program to decorate arithmetic operations.
def arithmetic_oprations(func):
    def operators(a,b):
        func(a,b)
        print("The product is:",a*b)
        print("The division is:",a/b)
        print("The remainder is:",a%b)
    return operators
print("This is a decorted function")
@arithmetic_oprations
def add_and_subtract(a,b):
    print("The addition is:",a+b)
    print("The sutraction is:",a-b)
add_and_subtract(20,10)
