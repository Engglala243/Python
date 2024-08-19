class emp:
    name = "Adi"
    sal = 12000
    add = "Indore"
    lang = "Py"

    # def getInfo():       #This function show the error
    #     print(f"The language is {self.lang}. The salary is {self.sal}")

    def getInfo(self):
        print(f"The language is {self.lang}. The salary is {self.sal}")

    def great(self):
        print(f"The name is {self.name}. The address is {self.add}")

a = emp()
# a.getInfo()
emp.getInfo(a)
emp.great(a)