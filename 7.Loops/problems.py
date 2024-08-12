# ===========================> 1).
# table print
# n = int(input("Enter a no. : "))
# for j in range(1, 11):
#     print(f"{n} X {j} = {n*j}")


# using while
# n = int(input("Enter a no. : "))
# i = 1
# while i <= 10:
#     print(f"{n} X {i} = {n*i}")
#     i += 1


# ===========================> 2).
# find word using first character
# i = ["Adi","Aje","Sumit","Rahul"]
# for name in i:
#     if(name.startswith("A")):
#         print(f"Hello {name}")


# ===========================> 3).
# no. is prime or not
# n = int(input("Enter a no. : "))
# for i in range(2, n):
#     if(n%2==0):
#         print("No. is not prime")
#         break
# else:
#     print("No. is prime")


# ===========================> 4).
# sum of natural no.
# n = int(input("Enter a no. : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(f"Sum of natural no. is {sum}")

# using while
# n = int(input("Enter a no. : "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(f"Sum of natural no. is {sum}")


# ===========================> 5).
# factorial 
# n = int(input("Enter a no. : "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(f"Factorial of {n} is {fact}")


# ===========================> 6).
# pattern printing
# n = int(input("Enter a no. :"))
# for i in range(1, n+1):
#     # print(" "* (n-i), end="")
#     print("*"* i, end="")
#     # print("*"* (2*i-1), end="")
#     # print("*"* i, end="")
#     print("")


# ===========================> 7).
# pattern printing
# n = int(input("Enter a no. :"))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"* n,end="")
#     else:
#         print("*", end="")
#         print(" "*   (n-2), end="")
#         print("*", end="")
#     print("")


# ===========================> 8).
# reverse table print
n = int(input("Enter a no. :"))
for i in range (1, 11):
    print(f"{n} X {11 - i} = {n*(11-i)}")
