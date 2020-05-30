#6.Write a python program to generate Fibonacci Numbers upto 100 using generator.
def fab():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fab():
    if f>100:
        break;
    print(f)

