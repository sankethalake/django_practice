# Data Structures -> logical collection, Mani.

# Data Types -> type of data we will store

# list -> multi in single object, mutable(changed)

lil = []
print(type(lil))
print(lil)

li2 = [1, 2, 3, 4, 5]
print(li2)

li3 = [1, "Python", 3.4]
print(li3)

print(type(li3))

# index for list

print(li3[0])
print(li3[1])

print(li3[-1])

# type of object in list
print(type(li3[0]))
print(type(li3[1]))
print(type(li3[2]))

print(type(li3))

# list with list
li4 = [1, 2, 3]
li5 = [11, 22, li4]
print(li5)

print(li5[2][1])

# mutability : manipulating list already created
li6 = [1, 2, 3, 4, 5]

li6[2] = 33
print(li6)

# methods to manipulate list

#   insert(index, value) : insert object at given index
li6.insert(2, 99)
print(li6)

#   append() : add particular object at last of list
#           it takes object in single format
li6.append(77)
print(li6)

li6.append("satyam")
print(li6)

#   extend() : to add more than one object, in form of iterable
#           takes object which are iterable, it extract
li6.extend("string")
print(li6)

#   len(): checks length of iterable object
print(len(li6))

#   remove(): removes the entered value
li6.remove(33)
print(li6)

#   clear() : delete all objects in the list, but structure is not deleted
li6.clear()
print(li6)

# to delete structure : del : it is keyword
del li6
# print(li6)

li7 = [3, 4, 55, 3, 72, 8]
print(li7)

#   sort() : to sort list
#       for reverse sort : sort(reverse=True)   #not give space in attributes
#       by default all attributes/ parameters are set false
li7.sort()
print(li7)

li7.sort(reverse=True)
print(li7)

#   index() : return the index of object passed
print(li7.index(55))

#   pop() : remove last element by default or pass index
#       remove() takes object and pop() takes index
li7.pop()  # remove last element
print(li7)

li7.pop(0)  # remove element at given index
print(li7)

#   + : concatenation of both list
li_one = [1, 2, 3, 4, 5]
li_two = [1, 2, 3, 4, 5]
li_three = li_one + li_two
print(li_three)

# addition of elements of lists which are at same index
li_four = [li_one[i] + li_two[i] for i in range(len(li_one))]
print(li_four)



lisz1 = [1, 2, 3, 4, 5]
lisz2 = [1, 2, 3, 4, 5]

# printing of elements at same index side by side
for b1, b2 in zip(lisz1, lisz2):
    print(b1, b2)

# printing of list1 as it is and list two in reversed order
for b1, b2 in zip(lisz1, reversed(lisz2)):
    print(b1, b2)

# ########################################################################
# please see line 140 for description
liNew = []
for b1, b2 in zip(lisz1, lisz2):
    liNew.append([b1, b2])

print(liNew)

liNew2 = [[b1, b2] for b1, b2 in zip(lisz1, lisz2)]
print(liNew2)

liNew3 = [b1 + b2 for b1, b2 in zip(lisz1, lisz2)]
print(liNew3)

# steps to get to above Output
#   create empty list as in 125
#   then write for loop in brackets of new list
#   then write req. logic for output in-front of for loop it will be appended to list
#       such as print elements, or print their addition, etc.