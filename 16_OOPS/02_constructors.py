class employee :
    def __init__(self,name,age,amount):
        self.name = name
        self.age = age
        self.amount = amount
    def getName(self):
        return self.name
    def getInfo(self):
        print(f"name is {self.name} and he is {self.age} years old and he has {self.amount} in the account .")


e1 = employee("manu",23,2563256)
print(e1.getName())
e1.getInfo()