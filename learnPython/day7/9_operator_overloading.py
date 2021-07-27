# Polymorphism
# Operator Overloading
class Add:
   #     num = int()                # no need for this statement

    def __init__(self, number):
        self.num = number           # self : it is used to initialize number for that particular objects
        print(self.num)

    def __add__(self, other):
        return self.num + other.num


a1 = Add(10)
a2 = Add(20)


print(a1 + a2)

# ##########################################################
# use of self: used to initialize something(here number) for particular object
class ReplaceInternal:
    def __init__(self,number):
        self.number = number
        print(self.number)

ril = ReplaceInternal()