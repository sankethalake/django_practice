# creating class

class House:
    room = 2            # members, properties, characteristics
    kitchen = 1
    hall = 2
    area = int()        # if we not want to set default values


niwas = House()           # niwas, Ghar are reference variables
Ghar = House()

print(niwas.kitchen)
print(niwas.room)
print(niwas.hall)
print(niwas.area)

print(Ghar.hall)

