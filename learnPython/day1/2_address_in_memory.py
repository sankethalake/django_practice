num1 = 10
num2 = 10

print(id(num1))  # id of both references is same when same value is stored
print(id(num2))

num1 = 20       # when we change value of num1 the id is also changed
print(id(num1))

print(num2)
print(id(num2))


