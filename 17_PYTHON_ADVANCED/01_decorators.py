
def decorators(fun):
    def wraper():
        print("something is going to be printed")
        fun()
        print("something is printed")
    return wraper    
        

@decorators
def printHaii():
    print("Haiii")   
 
printHaii()  




# def printHaii():
#     print("Haiii")
# f = decorators(printHaii)

# f()