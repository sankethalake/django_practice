# Tuple -> immutable (can't  change , add , del ,update)
tup1 = ()
print(type(tup1))
print(tup1)

#
tup2 = (1, 2, 3, 4, 5)
print(tup2)

# heterogeneous tuple
tup3 = ("python", 1.4, 10)
print(tup3)

# index
print(tup3[0])
print(tup3[1])
print(tup3[2])
# print(tup3[4])

# taking tuple element in reference
tup_var = tup3[1]
print(tup_var)
print(type(tup_var))

tup_var = "java"
print(tup_var)

print(tup3)

# tuple don't support item assignment
#tup3[0] = "java"

# methods in tuple
#   count() : give the count of element provided
tup11 = (1, 2, 3, 4, 5)
print(tup11.count(3))


tup12 = (1, 2, 2, 2, 3, 4, 5, 2)
print(tup12.count(2))  # gives index of first 2
print(tup11.index(2))
# +
tup_new = tup12 + tup11
print(tup_new)

# list inside tuple
#   we can add, modify, delete the element inside list present in tuple
#   but can't modify tuple
tupList = ([1, 2, 3, 4, 5], [11, 2, 3, 4, 5])

tupList[0][1] = 99
print(type(tupList[0]))
print(type(tupList))
print(tupList)


tupList[0].append(6)
print(tupList)

# tuple inside list
#   here we can do changes in list but not inside tuple
listTup = [(1, 2, 3), (1, 2, 33)]
print(listTup)

print(listTup[0])

# listTup[0][2] = 99      tuple object does not support item assignment

listTup.pop()
print(listTup)

# Extract element into references
tupExtract = (1, 2, 3, 4, 5)

a, b, c, d, e = tupExtract

print(a, b, c, d, e)
print((type(a)))

# swapping
tupSwap = (1, 2, 3)
tupSwap1 = (11, 22, 33)

tupSwap, tupSwap1 = tupSwap1, tupSwap
print(tupSwap)
print(tupSwap1)

# add element 4,5 in new tuple
tup20 = (1, 2, 3, 4, 5, 6)
tup_new = tup20[3:5]
tup20 = (1, 2, 3)
print(tup20)
print(tup_new)
