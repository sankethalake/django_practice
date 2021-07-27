# __init__() : used for initialization
#    not need to call explicitly, called when object is created
#   also called as magic methods and
#   there is only one __init__() method for class
#   this is not a constructor
class Student:
    def insertValues(self, nameIs, lnameIs, rollNois):
        name = nameIs
        lname = lnameIs
        rollNo = rollNois

        print("name is", name)
        print("lname is", lname)
        print("rollNo is", rollNo)

    def __init__(self, nameIs, lnameIs, rollNois):
        name = nameIs
        lname = lnameIs
        rollNo = rollNois

        print(name, " ", lname, " ", rollNo)


std1 = Student("Satyam", "Raj", 4)
std2 = Student("Palash", "Doshi", 23)

std1.insertValues("Suraj", "Thorat", 8)
std2.insertValues("Nishant", "Goshke", 2)
