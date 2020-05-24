'''
3.Print the pattern
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
'''
n=int(input("Enter number of rows you want:"))
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
