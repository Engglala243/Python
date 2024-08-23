# custom exception
try:
    a = int(input("Enter a Ist value : "))
    b = int(input("Enter a IInd value : "))


except ValueError as v:
    print(f"Invalid input. Please enter a valid integer. ====> {v}")

except ZeroDivisionError as z:
    print(f"Error: Division by zero is not allowed. ====> {z}")

if(b == 0):
    raise ZeroDivisionError("Invalid input. Please enter a valid input on interger values")
    
else:
    print(f"Division of {a} and {b} is {a/b}")
