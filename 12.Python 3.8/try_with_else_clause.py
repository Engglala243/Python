try:
    a = int(input("Enter a value : "))
    print(a)

except Exception as e:
    print(f"Invalid input ==> {e}")

else:
    print("No exception occurred")