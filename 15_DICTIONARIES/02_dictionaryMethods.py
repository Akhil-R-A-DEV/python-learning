marks = {"Anu":20,"Manu":18,"Sam":25}

print(marks)

marks["Anu"] = 21

print(marks)

print(marks.keys())
print(marks.values())

marks.pop("Manu")
print(marks.values())