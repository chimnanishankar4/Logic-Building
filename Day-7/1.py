'''
1.Write python program to perform bank operations using class and objects.
Conditions:
a.Bank name should be static.
b.Using menu driven program.
1 Deposit
2. Withdraw
3. Exit
'''
import sys
class Customer:
    bankname="SBI"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Balance is:",self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Sufficient balance ",self.amount)
            sys.exit()
        self.balance=self.balance-amount
        print("The balance after withdraw:",self.balance)
print("Welcome to",Customer.bankname)
name=input("Enter your name:")
c=Customer(name)
while True:
    print("d-Deposite\nw-Withdraw\ne-Exit")
    option=input("Choose your choose:").lower()
    if option=='d':
        amount=float(input("Enter amount to Deposite:"))
        c.deposit(amount)
    elif option=='w':
         amount=float(input("Enter amount to Withdraw:"))
         c.withdraw(amount)
    elif option=='e':
        print("Thanks for banking")
        sys.exit()
    else:
        print("Invalid option please choose valid option")
    
