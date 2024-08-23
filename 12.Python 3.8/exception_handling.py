# Built in exception
try:
    a = int(input("Enter the value : "))
    print(a)

# except ValueError as v:
#     print(f"Invalid input. Please enter a valid integer. ====> {v}")

except Exception as e:
    print(f"An error occurred: {e}")