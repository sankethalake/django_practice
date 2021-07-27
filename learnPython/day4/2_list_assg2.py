# first element of list1 with last element of list2 and so on

lis1 = [1, 2, 3, 4, 5]
lis2 = [1, 2, 3, 4, 5]

#   using reversed keyword
for b1, b2 in zip(lis1, reversed(lis2)):
    print(b1, b2)

#   using slice
for b1, b2 in zip(lis1, lis2[::-1]):
    print(b1, b2)
