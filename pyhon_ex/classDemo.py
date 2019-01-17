
class Computer: # class declaration

    def __init__(self,a,b): # constructor
        self.a = a
        self.b = b

    def __config(self):
        print("1TB,16 GB Ram,i3")

    def add(self):
        c = self.a + self.b
        print('add', c)

# instance of a class

com1 = Computer(2,4)
com2 = Computer(1,5)


com1.add()
com2.add()