
class Printer(object):
    def __init__(self):
        self.String = " "

    def getString(self):
        self.String = str(input())

    def printString(self):
        print(self.String.upper())

a = Printer()
a.getString()
a.printString()
