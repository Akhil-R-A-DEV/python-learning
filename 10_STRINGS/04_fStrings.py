template = "This is {} and he have ${}"
a="Akhil"
a1=300000
b="Manu"
b1=200000
c="Raj"
c1=100000

aData = template.format(a,a1)
print(aData)

bData = template.format(b,b1)
print(bData)

cData = template.format(c,c1)
print(cData)


print(f"Name is {a} and he has ${a1}")