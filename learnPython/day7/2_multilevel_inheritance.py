# inheritance
#   multi level inheritance:

class GrandParent:
    def terminate(self):
        print("this is GP method")

class Parent(GrandParent):
    def display(self):
        print("this is Parent method")

class Infant(Parent):
    def show(self):
        print("this is Infant method")

i1 = Infant()
i1.show()
i1.terminate()
i1.display()
