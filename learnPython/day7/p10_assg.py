# add three objects using operator overloading

class Add:

    def __init__(self, number):
        self.num = number           # self : it is used to initialize number for that particular objects
        print(self.num)

    def __add__(self, other):
        return self.num + other.num


a1 = Add(10)
a2 = Add(20)
a3 = Add(30)


print(a1 + a2 + a3)