class A(object):
    def __init__(self):
        self.someProperty = 5

    def someHardMethod(self):
        print("do hard things")


class B(A):
    pass


b = B()
b.someHardMethod()
b.someProperty = 45
