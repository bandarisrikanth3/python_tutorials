
class Computer:
    school ="welcome to oops" # static class variables


    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def compare(self,c2):
        if self.age == c2.age:   # instnace variables
            return True
        else:
            return False;

    @classmethod
    def getSchool(self):
        return self.school

    @staticmethod
    def info():
        print("This is for information")

    



c1 = Computer()
c1.name = 'srikanth'
c1.age=28
c2 = Computer()

print(c1.name,c1.age)
print(c2.name,c2.age)

if c1.compare(c2):
    print("same")
else:
    print("different")
print(c1.school)
Computer.default = 234

print(c1.school)

print(Computer.getSchool())