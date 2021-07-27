# polymorphism
#   real life eg. Man can be son, father, husband ,etc.

# Overloading, Overridding

# method overloading not possible in python
# Method loading ->
class Poly:
    def add(self, num1,num2):
        print(num1 + num2)

    def add(self,num1,num2,num3):
        print(num1 + num2)

p1 = Poly()
# p1.add(20,30)             # if we run this line it will show error as method gets overrrided
p1.add(10,20,30)


