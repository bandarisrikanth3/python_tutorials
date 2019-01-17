
class A:

    def show(self):
        print("in A class")

class B(A):
    pass

a = B()

print(a.show())