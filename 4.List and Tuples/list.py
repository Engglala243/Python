group = ["Ajeet",2,True,"Akash",1,False]
print(group)
print(group[1])
print(group[1:4])

group[2] = False #unlike string list are mutable
print(group[0:4])
print(group)

group.append("Anshul") #add at the end of this list
print(group)