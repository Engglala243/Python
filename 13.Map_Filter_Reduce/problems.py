# find divisible by 5
# def divi(n):
#     if(n%5==0):
#         return True
#     return False

# a = [22,3,45,65,75,50,555555,22222225555]
# f = list(filter(divi, a))
# print(f)

from functools import reduce
a = [22,3,45,65,75,50,55,225]

def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater, a))
