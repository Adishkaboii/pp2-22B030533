import math

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)

    def move(self):
        x1 = int(input())
        y1 = int(input())
        self.x = x1
        self.y = y1

    def dist(self):
        x1 = int(input())
        y1 = int(input())
        z = (x1 - self.x)*(x1 - self.x)+(y1 - self.y)*(y1 - self.y)
        print(math.sqrt(z))
    
a = int(input())
b = int(input())
p = Point(a, b)
p.show()
p.move()
p.show()
p.dist()
