class emp:
    name = 'Adi'
    lang = 'Py'      #class attribute
    sal = 12000

a = emp()
a.sal = 15000        #object/instance attribute higher preference as comparision of class attribute
print(a.name,a.sal,a.lang)