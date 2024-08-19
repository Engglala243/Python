class Emp:
    company = 'ITC'
    name = "Adi"
    def show(self):
        print(f"The name of the Emp is: {self.name}, and the company is: {self.company}")

class Coder:
    lang = 'Py'
    def printLang(self):
        print(f"The language of the coder is: {self.lang}")

class Prog(Emp,Coder):
    company = 'Apoliums'
    def showLang(self):
        print(F"The Company is {self.company} and he is good with {self.lang} language")

b = Prog()

b.show()
b.showLang()
b.printLang()