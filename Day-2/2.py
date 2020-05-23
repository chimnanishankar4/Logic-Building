#Write a program to count how many even and odd numbers in list 
even_count=0
odd_count=0
list=[1,2,3,4,5,6,7,8,9,10]
for num in list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Number of even cound:",even_count)
print("Number of odd cound:",odd_count)

    
    
