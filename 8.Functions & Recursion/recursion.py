def fun(n):
    if (n == 0 or n == 1):
        return 1
    return n * fun(n-1)
n = int(input("Enter a no. :"))
print(f"The factorial of this number is : {fun(n)}")
