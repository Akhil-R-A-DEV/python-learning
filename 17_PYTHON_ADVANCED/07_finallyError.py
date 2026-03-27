a = int(input("Enter 1st num : "))
b = int(input("Enter 2nd num : "))


try:
    c = a/b
except Exception as e:
    print("something went wrong",e)
else :
    print("all good")
finally:
    print("end")            