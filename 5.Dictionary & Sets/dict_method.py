marks = {
    "Ajeet" : 10,
    "Akash" : 9,
    "Anshul" : 7,
    0: "Adi "
}
print(marks.keys())
print(marks.values())

marks.update({"Ajeet":8})
marks.update({"Akash":8, "Deepak":5})
print(marks)


# print(marks.get("Ayush")) :- (return None) ye dono line ka kam ak hi hai but .get method error nhi hai agr key value dict me nhi hai to or jo second line hai vo error deti hai
# print(marks["Ajeett"]) :- (return error)