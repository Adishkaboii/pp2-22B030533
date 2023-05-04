class Shape():
    def __init__(self):
        pass

    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, len = 0):
        Shape.__init__(self)
        self.len = len

    def area(self):
        print(self.len*self.len)

a = int(input())
s = Shape()
s.area()
y = Square(a)
y.area()
