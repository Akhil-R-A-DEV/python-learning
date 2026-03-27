class employee:

    company = "hp"

    def __init__(self,name,amount):
        self.name = name 
        self.amount = amount 

    #instanceMethod
    def getName(self):
        return self.name
    
    @staticmethod
    def sum(a,b):
        return(a+b)
    
    @classmethod
    def changeCompany(cls,newCompany):
        newCompanyName = newCompany
        cls.company = newCompanyName
        print(cls.company)



e1 =employee("unni",85000)
e2=employee("manu",79000)

print(employee.company)
print(e1.company)
print(e1.sum(3,7))
e1.changeCompany("acer")

print (employee.company)
