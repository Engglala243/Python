# factorial
# def greatest(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(greatest(6,5,4))

# fari. to cel. with round of two decimal place and show the degree
# def fari_to_cel(f):
#     return 5*(f-32)/9
# f = int(input("Enter the value :"))
# c = fari_to_cel(f)
# print(f"{c:.2f}°C")  
# print(f"{round(c,2)}°C")  

# remove next line printing
# print("a")
# print("b")
# print("c", end="")
# print("d", end="")

# sum n natural no.
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n 
# print(sum(10))

# pattern printing
# def fun(n):
#     if(n==0):
#         return
#     print("*" * n)
#     fun(n-1)    
# n = fun(int(input("Enter a value :")))

# convert inchs to cm
# def fun(n):
#     return n * 2.54
    
# m = fun(int(input("Enter a no. :")))
# print(fun(m))

# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
# l = ["adi","rohan","subham","anthe"]
# print(rem(l, "an"))

# table print
# def fun(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")
# fun(2)