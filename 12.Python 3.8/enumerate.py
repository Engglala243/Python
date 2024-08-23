l = [2,3,4,5,6]

# long way 
index = 0
for itme in l:
    print(f"{index} and {itme}")
    index += 1

# simplified way
for index, item in enumerate(l):
    print(f"Index: {index}, Item: {item}")