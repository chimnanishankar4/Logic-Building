'''
write pattern like this
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
n=int(input("Enter number of rows:"))
for i in range(1,n+1):#0,1,2,3,4
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    

