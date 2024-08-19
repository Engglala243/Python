class Emp:
    a = 1

class Pro(Emp):
    b = 2

class Manag(Pro):
    c = 3

o = Emp()
# print(o.__class__.__name__) 
print(o.a)

o = Pro()
print(o.a, o.b)

o = Manag()
print(o.a, o.b, o.c)