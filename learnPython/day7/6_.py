# init() of parent is implicitly called when we create object of child class and init() is not present in child class


class Parent:
    def __init__(self):
        print("this is init method of parent")

    def show(self):
        print("this is show method of parent")


class Child(Parent):
    pass


c1 = Child()  # here init() of parent is callec
c1.show()
