def outer(num1, num2):
    def inner(num1, num2):
        return num1 - num2

    result = inner(num1, num2)
    print(result ** 3)


outer(4, 1)


