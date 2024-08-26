from functools import reduce
l = [1,2,3,4,5]
# map
square = lambda x: x*x/2

sqList = map(square, l)
print(list(sqList))

# filter
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# reduce
def sum(a,b):
    return a + b
print(reduce(sum, l))