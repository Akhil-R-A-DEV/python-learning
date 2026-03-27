class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return point(self.x+other.x,self.y+other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
        

a = point(1,3)
b = point(2,6)
c = a+b


print(c)
