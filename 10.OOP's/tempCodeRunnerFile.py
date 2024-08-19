class calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return self.num ** 0.5

a = calculator(int(input("Enter a number :")))
print(f"Square of {a.num} is {a.square()}")
print(f"Cube of {a.num} is {a.cube()}")
print(f"Square root of {a.num} is {a.square_root()}")
