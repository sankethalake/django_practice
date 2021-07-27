# duck typing : if it quake like duck, it is duck

#       knowing object belongs to which class on basis of its properties
#       by passing object check object belongs to which class...by its properties
class Bird:
    def fly(self):
        print("belongs to bird class")

class Human:
    def walk(self):
        print("belongs to human class")

class Fish:
    def swim(self):
        print("belongs to fish class")

def access(self):
    # self.swim()
    self.walk()
    # self.fly()


Donald = Bird()
Niraj = Human()
Dora = Fish()

access(Niraj)