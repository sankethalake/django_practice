# if init() is present in parent as well as child which will be  called?
#   init() from child will be called
#       init() is not  a constructor

class Parent:
    def __init__(self):
        print("this is init method of parent")


class Child(Parent):
    def __init__(self):
        print("this is init method of child")


c1 = Child()