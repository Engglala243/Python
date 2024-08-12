#===========================> 1).
# words = {
#     "madad" : "Help",
#     "kya" : "What",
#     "kursi" : "Chair",
#     "billi" : "Cat"
# }
# word = input("Enter the word :")
# print(words[word])

#===========================> 2).
# s = set()
# n = input("Enter number :")
# s.add(int(n))
# n = input("Enter number :")
# s.add(int(n))
# n = input("Enter number :")
# s.add(int(n))
# n = input("Enter number :")
# s.add(int(n))
# print(s)

#===========================> 3).
# s = set()
# s.add(18)
# s.add('18')
# print(s)

#===========================> 4).
# s = set()
# s.add(20)
# s.add(20.0)
# s.add(20.5)
# s.add('20')
# print(s)
# print(len(s))

#===========================> 5).
# s = {}
# print(s, type(s))

#===========================> 6).
# value same ho skti hai but key same hui to value update ho jaye gi
d = {}

name = input("Enter name :")
lang = input("Enter language name :")
d.update({name:lang})

name = input("Enter name :")
lang = input("Enter language name :")
d.update({name:lang})

name = input("Enter name :")
lang = input("Enter language name :")
d.update({name:lang})

name = input("Enter name :")
lang = input("Enter language name :")
d.update({name:lang})

print(d)
