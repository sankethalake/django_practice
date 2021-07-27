# INPUT from user
#   by default input() takes string as input

takeInput = input("Enter value - ")
takeInput2 = input("Enter value - ")

print((takeInput + takeInput2))
print(type(takeInput))
print(type(takeInput2))

#   for taking integer as input, we take input and convert it to int

takeInputInt = int(input("Enter num1 = "))
takeInputInt2 = int(input("Enter num2 = "))

print(takeInputInt + takeInputInt2)
print(type(takeInputInt))
print(type(takeInputInt2))
