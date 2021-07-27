# what will be output: method1
class Test:
    def __init__(self):
        print("this is init method1")


    def _init_(self):
        print("this is init method2")


    def init(self):
        print("this is init method3")


t1 = Test()

# #######################################################

# what will be output of following program : compile time error
#   only recent one will be called as it overrides all other methods
class Test1:
    def __init__(self):
        print("this is init method1")


    def __init__(self, num1):
        print("this is init method2")


    def __init__(self, num2, num3):
        print("this is init method3")


t1 = Test1()