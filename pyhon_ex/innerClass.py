
class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()
    
    def show(self):
        print("name: {} and age: {}".format(self.name,self.age))
        self.lap.show()


    class Laptop:
        company = "HP"

        def __init__(self):
            pass

        @staticmethod
        def show():
            print("PC 123")


        @classmethod
        def get_company(cls):
            return cls.company


s1 = Student('srikanth',24)

s1.show()

print(Student.Laptop.get_company())