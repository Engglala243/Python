class Emp:
    company = "Apoliums"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Google"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLang(self):
#         print(f"The programmer knows {self.lang}")

class Programmer(Emp):
    company = "Google"
    def showlang(self):
        print(f"The programmer knows {self.lang}")
        
a = Emp()
b = Programmer()

print(a.company, b.company)