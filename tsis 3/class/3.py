class Shape():
    def __init__(self):
        pass

    def area(self):
        print(0)

class Rectangle(Shape):
    def __init__(self, width=0, length=0):
        Shape.__init__(self)
        self.width = width
        self.length = length

    def area(self):
        print(self.width*self.length)

z = Rectangle(4,5)
z.area()
