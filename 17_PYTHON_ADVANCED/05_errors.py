# while True:
#     try:
#         a = int(input("Enter 1st num : "))
#         b = int(input("Enter 2nd num : "))
#         c = a/b
#         print(c)
#     except ZeroDivisionError :
#         print("cant devide by 0")

#     except Exception as e:
#         print("something went wrong",e)    


a = int(input("Enter 1st num : "))
b = int(input("Enter 2nd num : "))

if b == 0:
    raise ValueError("cant devide by 0")
print(a/b)