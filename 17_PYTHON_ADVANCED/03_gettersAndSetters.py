# class employee:
#     def __init__(self,name,amount):
#         self.name = name 
#         self.amount = amount 

#     def getName(self):
#         return self.name
#     def getFirstName(self):
#         nameToList = self.name.split(" ")
#         fnane = nameToList[0]
#         print (nameToList)
#         return fnane
#     def setFirstName(self , nName):
#         nameToList = self.name.split(" ")
#         newName = f"{nName} {nameToList[1]}"
#         return newName


# e = employee("unni ak",86565656)

# print(e.getName())
# print(e.getFirstName())
# print(e.setFirstName("the"))




class employee:
    def __init__(self,name,amount):
        self.name = name 
        self.amount = amount 

    def getName(self):
        return self.name
    @property
    def FirstName(self):
        nameToList = self.name.split(" ")
        fnane = nameToList[0]
        print (nameToList)
        return fnane
    
    @FirstName.setter
    def FirstName(self , nName):
        nameToList = self.name.split(" ")
        newName = f"{nName} {nameToList[1]}"
        self.name = newName
      


e = employee("unni ak",86565656)

print(e.FirstName)
e.FirstName = "haha"
print(e.name)