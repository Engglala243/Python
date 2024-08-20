# =================== 1).
# class TwoDVector:
#     def __init__(self,i ,j):
#         self.i = i
#         self.j = j

#     def show(self): 
#         print (f"The vector is {self.i}i and {self.j}j")

# class ThreeDVector(TwoDVector):
#     def __init__(self,i ,j, k):
#         super().__init__(i,j)
#         self.k = k

#     def show(self):
#         print (f"The vector is {self.i}i and {self.j}j and {self.k}k")

# a = TwoDVector(1, 2)
# a.show()

# b = ThreeDVector(3, 4, 4)
# b.show()    


# =================== 2).
# class Animals:
#     print("The Animals class")

# class Pets(Animals):
#     print ("The Pwts class")

# class Dog(Pets):

#     @staticmethod
#     def bark():
#         print("Bow Bow..!")

# d = Dog()
# d.bark()


# =================== 3).
# class Employee:
#     def __init__(self, salary=200):
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

#     def increment_salary(self, increment=20):
#         self.salary += increment

# e = Employee()
# print(e.get_salary())
# e.increment_salary()
# print(e.get_salary())


# =================== 4).
# class Emp:
#     salary = 234
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((salary/self.salary)-1)*100

# e = Emp()
# e.salaryAfterIncrement = 280
# print(e.increment)

# =================== 4).
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1*c2)