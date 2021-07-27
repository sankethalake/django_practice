# Method overriding
# req: two classes with inheritance having same method name with different logic

class Parent:
    def show(self):
        print("this is 11990s Mobile")


class Child(Parent):
    def show(self):
        print("this is 11990s logic + Enhanced features")


c1 = Child()
c1.show()
