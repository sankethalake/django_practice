tup11 = (1, 2, 3, 4, 5)
a = tup11[0]
b = tup11[1]
c = tup11[2]
d = tup11[3]
e = tup11[4]

print(a, b, c, d, e)

##
a, b, c, d, e = tup11
print(a, b, c, d, e)


tupSwap = (1, 2, 3)
tupSwap1 = (11, 22, 33)

# tuptemp = tupSwap
# tupSwap = tupSwap1
# tupSwap1 = tuptemp

tupSwap, tupSwap1 = tupSwap1, tupSwap
print(tupSwap,tupSwap1)

print(tupSwap)
print(tupSwap1)


def fun(index_list):
    tup20 = (10, 20, 30, 40, 50, 60)
    lis = []
    for index in index_list:
        lis.append(tup20[index])
    tup_new = tuple(lis)
    print(tup_new)


fun([3, 4])

# simplest
tup20 = (1, 2, 3, 4, 5, 6)
tup_new1 = tup20[3:5]

print(tup_new1)
