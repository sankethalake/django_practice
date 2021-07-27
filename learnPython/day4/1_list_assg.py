# addition of elements of lists which are at same index

def add_list(li1, li2):
    li3 = []

    length = len(li1)

    for index in range(length):
        print(index)
        li3.append((li1[index] + li2[index]))

    print(li3)

li1 = [1, 2, 3, 4]
li2 = [5, 6, 7, 8]

add_list(li1,li2)



######################################################################
l1 = [1, 1, 1, 1, 1]
l2 = [2, 2, 2, 2, 2]

for i in range(0,4) :
    print(l1[i] + l2[i])