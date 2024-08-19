class Emp:
    a = 1
    def __init__(self):
        print("Emp Class Constructor")

class Pro(Emp):
    b = 2
    def __init__(self):
        print("Pro Class Constructor")


class Manag(Pro):
    c = 3
    def __init__(self):
        super().__init__()
        print("Manag Class Constructor")



o = Manag()
print(o.a, o.b, o.c)