'''
3.Given the triangle of consecutive odd  numbers
                        1
                    3      5
                 7      9      11
            13      15     17     19
Above triangle is given Calculate Sum of row wise 
Example we call function :- row_sum_odd_numbers(2)
Result will be=3+5=8

'''

'''
Solution 1
def row_wise_sum(n):
    return n*n*n
print("The sum of rows:",row_wise_sum(4))
'''
'''
Solution 2
def row_wise_sum(n):
    return pow(n,3)
print("The sum of rows:",row_wise_sum(4))
'''
'''
solution 3
row_wise_sum=lambda n:n**3
print("The sum of rows:",row_wise_sum(4))
'''
#solution 4
def row_wise_sum(n):
    return n**3
print("The sum of rows:",row_wise_sum(4))
