class emp:
    name = "Adi"
    sal = 12000
    add = "Indore"
    lang = "Py"

    def __init__(self, name, sal, lang):           #dunder method which is automatically call
        self.name = name
        self.sal = sal
        self.lang = lang    
        print("This is the constructor")

    # def getInfo():       #This function show the error
    #     print(f"The language is {self.lang}. The salary is {self.sal}")

    def getInfo(self):
        print(f"The language is {self.lang}. The salary is {self.sal}")

    def great(self):
        print(f"The name is {self.name}. The address is {self.add}")

    


a = emp("Ajeet", 100011, ".net")
print(a.name,a.sal,a.lang)
# a.getInfo()
emp.getInfo(a)
emp.great(a)