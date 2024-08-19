class Emp:
    a = 1

    @classmethod
    def show(cls):
        print(cls.a)

    @property
    def name(self):
        return f"{self.__fname} and {self.__lname}"

    @name.setter
    def name(self, value):
        self.__fname = value.split(" ")[0]
        self.__lname = value.split(" ")[1]
        
e = Emp()
e.name = "Aje Raj"

print(e.name)

e.show()
