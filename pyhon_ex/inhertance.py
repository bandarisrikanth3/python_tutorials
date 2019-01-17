class A:
    def __init__(self):
        print("init A")

    def feture1(self):
        print("feature1")

    def feture2(self):
        print("feature1")


class B:
    def __init__(self):
        print("init B")

    def feture3(self):
        print("feature1")

    def feture4(self):
        print("feature1")

class C(B,A):
    def __init__(self):
        super().__init__();
        print("init C")

    def feture5(self):
        print("feature1")

    def feat(self):
        super().feture1()



details = C()
details.feat()
