# inheritance
#   Hi. inheritance

class Parent:
    def terminate(self):
        print("this is Parent method")

class Infant2(Parent):
    def display(self):
        print("this is infant2 method")

class Infant(Parent):
    def show(self):
        print("this is Infant method")