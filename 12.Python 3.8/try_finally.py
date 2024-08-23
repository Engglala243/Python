# correct way to use final keyword in function
def main():
    try:
        a = int(input("Enter a value :"))
        print(a)
        return

    except Exception as e:
        print(f"Invalid input ==> {e}")
        return

    finally:
        print("Program ended")

    print("Program ended with using finally") 

main()

# wrrong way ro use without unsing function
# try:
#     a = int(input("Enter a value :"))
#     print(a)

# except Exception as e:
#     print(f"Invalid input ==> {e}")

# finally:
#     print("Program ended")

# print("Program ended with using finally") 