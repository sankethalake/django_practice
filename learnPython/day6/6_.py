# methods of class with parameters and use of self keyword

class Arith:
    def add(self, num1, num2):  # must write self as first paramenter
        print(num1 + num2)  # if we change position of self it gives error


obj = Arith()
obj.add(10, 20)

# self keyword : pass the object reference so that method will know to whom it have to give answer

sampada = Arith()
nishant = Arith()

sampada.add(10,20)
nishant.add(30,50)


# other way to call a method and verify use of self keyword

Arith.add(sampada,50,50)