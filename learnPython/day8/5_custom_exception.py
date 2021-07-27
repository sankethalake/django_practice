# custom exception
#   raise is similar to throw
class TryAgainNotClearedError(Exception):
    def __init__(self, emessage):
        self.emessage = emessage
        print(self.emessage)


value = int(input("Enter value - "))

if value < 40:
    raise TryAgainNotClearedError("marks not valid")

else:
    print("pass")