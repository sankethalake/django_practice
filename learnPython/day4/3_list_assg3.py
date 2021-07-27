# question --> [1,2,3,4,5,3]
# output --> [1,2,30,4,5,3]

lis1 = [1, 2, 3, 4, 5, 3]

# index = lis1.index(3)
# lis1[index] = 30
# print(lis1)

for index in range(len(lis1)):
    if lis1[index] == 3:
        lis1[index] = 30
        break
print(lis1)


# user user input list
# question2 --> [11,2,3,4,5,1,2,5,3,4,5,5]


def fun():
    lis = []
    n = int(input("Enter the no of values to be enter"))
    print("enter the values")
    for i in range(n):
        element = int(input())
        if element in lis:
            continue
        else:
            lis.append(element)
    print(lis)


fun()
