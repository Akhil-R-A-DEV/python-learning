class employee:
    company = "abcdCompany"
    def __init__(self,name,age,company):
        self.name = name
        self.age = age
        self.company = company

    def getCompany(self):
        return self.company

e1 = employee("namu",20,"123company")
print(e1.getCompany())
print(employee.company)