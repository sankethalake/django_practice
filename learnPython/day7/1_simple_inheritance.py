# inheritance
#   simple inheritance

class Parent:
    def show(self):
        print("This is Parent Method")


class Child(Parent):                        # simple inheritance
    def display(self):
        print("This is Child Method")


p1 = Parent()
p1.show()

c1 = Child()    # child can access Parent class methods as it inherited Parent class
c1.display()
c1.show()