#Write a program to add natural numbers
sum=0
n=int(input("Enter number:"))
for i in range(1,n):
    sum+=i
    print(i," + ",end="")
sum+=n
print(n," = ",sum)
    
