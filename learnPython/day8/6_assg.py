# voting with custom exception

class LessThanRequiredAge(Exception):
    def __init__(self):
        print("Age is less than required")


class MoreThanRequiredAge(Exception):
    def __init__(self):
        print("Äge is more than required")


age = int(input("Enter the age - "))

if age < 20:
    raise LessThanRequiredAge
elif age > 30:
    raise MoreThanRequiredAge
else:
    print("You can vote")



