class Student:
    def insertValues(self,nameIs, lnameIs,rollNois):
        name = nameIs
        lname = lnameIs
        rollNo = rollNois

        print("name is", name)
        print("lname is", lname)
        print("rollNo is", rollNo)


std1 = Student()
std2 = Student()

std1.insertValues("Suraj", "Thorat", 8)
std2.insertValues("Nishant", "Goshke", 2)