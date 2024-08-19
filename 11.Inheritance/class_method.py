class Emp:
    a = 1

    @classmethod
    def show(cls):
        print(cls.a)

e = Emp()
e.a = 4

e.show()