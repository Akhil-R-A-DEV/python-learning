# with open("18_FILE_IO/Read file.txt", "r") as readFile:
#     f = readFile.read()
#     print(f)

readFile = open("18_FILE_IO/Read file.txt", "r")
f = readFile.read()
print(f)

readFile.close()