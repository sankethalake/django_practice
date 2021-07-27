# inheritance
# multiple inheritance

class Parent1:
    def terminate(self):
        print("this is parent1 method")

class Parent2:
    def display(self):
        print("this is parent2 method")

class Infant(Parent1,Parent2):
    def show(self):
        print("this is infant method")


i1 = Infant()
i1.terminate()
i1.display()
i1.show()