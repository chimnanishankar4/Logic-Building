#4.Accept data in two 3*3 matrix and calculate the sum of the matrices.
x=[[1,2,3],
   [4,5,6],
  [7,8,9]]
y=[[1,2,3],
   [4,5,6],
   [7,8,9]]
result=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for x in result:
    print(x)
