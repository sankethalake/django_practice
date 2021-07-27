# all different types to write a function with parameters

def demo():
    print("this is default")


demo()


# --------------------------------------------------------------------------------

def para(num):
    print("this is parameterised function ", num)


para(10)


# --------------------------------------------------------------------------------

def para2fun(num1, num2):
    print(num1)
    print(num2)


para2fun(10, 20)


# --------------------------------------------------------------------------------

def para3fun(num1, num2=40):
    print(num1)
    print(num2)


para3fun(10)


# --------------------------------------------------------------------------------

def para4fun(num1=50, num2=40):
    print(num1)
    print(num2)


para4fun()
para4fun("Palash", "Doshi")
para4fun(1.2, 2.3)


# --------------------------------------------------------------------------------

def para5fun(num1, num2):
    print("num1= ", num1)
    print("num2= ", num2)


para5fun(71, 70)
para5fun(num2=71, num1=70)


# --------------------------------------------------------------------------------

def para6fun(num1, num2):
    print(num1)
    print(num2)


# para6fun(10)
para6fun(num1=30, num2=40)


# --------------------------------------------------------------------------------

def para7fun(*num1):
    print(num1)


para7fun(1, 2, 3, 4, 5, 6)


# --------------------------------------------------------------------------------


def para8fun(*num1, num2=40):
    print(num1)
    print(num2)


para8fun(1, 2, 3, 4, 5, 6)


# --------------------------------------------------------------------------------

def para9fun(num1, *num2):
    print(num1)
    print(num2)


para9fun(1, 2, 3, 4, 5, 6)


# --------------------------------------------------------------------------------

def para10fun(num1, *num2):
    print(type(num1))
    print(type(num2))


para10fun(1, 2, 3, 4, 5, 6)

