# Few programmers working at microsoft

# class programmer:
#     company : "Microsoft"
#     def __init__(self, name, sal, pin):
#         self.name = name
#         self.sal = sal
#         self.pin = pin

# p = programmer("Aka", 200000, 454775)
# print(f"The employee name is {p.name}, salary is {p.sal}, pincode {p.pin}")
# r = programmer("Ajeet", 100000, 453441)
# print(p.name, p.sal, p.pin)
  

# calculator finding square, cube, squareroot
# class calculator:
#     def __init__(self, num):
#         self.num = num
    
#     def square(self):
#         return self.num ** 2

#     def cube(self):
#         return self.num ** 3

#     def square_root(self):
#         return self.num ** 0.5

# a = calculator(int(input("Enter a number :")))
# print(f"Square of {a.num} is {a.square()}")
# print(f"Cube of {a.num} is {a.cube()}")
# print(f"Square root of {a.num} is {a.square_root()}")

# create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o.Does this change the class attribute

# class Demo:
#     a = 10

# o = Demo()
# print(o.a) # print class attribute

# o.a = 5 
# print(o.a) # print instance attribute

# print(Demo.a)

# use staticmethod 
# class calculator:
#     def __init__(self, num):
#         self.num = num
    
#     def square(self):
#         return self.num ** 2

#     def cube(self):
#         return self.num ** 3

#     def square_root(self):
#         return self.num ** 0.5

#     @staticmethod
#     def add(a, b):
#         return a + b

# a = calculator(int(input("Enter a number :")))
# print(f"Square of {a.num} is {a.square()}")
# print(f"Cube of {a.num} is {a.cube()}")
# print(f"Square root of {a.num} is {a.square_root()}")
# print(a.add(4, 6)) # use static method without creating an object of the



from random import randint

class Train:
    # def __init__(self, trainNo):
    def __init__(slf, trainNo):
        # self.trainNo = trainNo
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f"Tickect is booked in train no: {self.trainNo} form {fro} to {to}")

    def getStatus(self):
        print(f"Tickect no: {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Tickect fare in train no: {self.trainNo} form {fro} to {to} is {randint(1111, 9999)}")

t = Train(12009)
t.book("Indore","Ujjain")
t.getStatus()
t.getFare("Indore","Ujjain")