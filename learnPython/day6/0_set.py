# sets :
#   contain unique values
#   sets don't have indexing    i.e unordered
#   mutable

setEmpty = set()
print(setEmpty)
print(type(setEmpty))

setEmpty.add(1)
print(setEmpty)
print(type(setEmpty))

set1 = {}  # this gives type as dict and not set
print(set1)
print(type(set1))

set2 = {1, 2, 3, 4, 5}  # when we not give key-value pair inside {} and only elements it becomes pair
print(set2)
print(type(set2))

#   set has unique values
set3 = {1, 2, 2, 2, 3, 4, 5}
print(set3)

# sets are unordered (don't have indexes)(ordered and sorted is different)
set4 = {1, 2, 4, 3, 5, 6}  # here it is sorted by chance(will not be sorted everytime)
print(set4)

set5 = {1, 2, 3, 4, 5}
print(set5)

#    operations on set using methods
set6 = {1, 2, 3, 4, 5}
print(set6)

set7 = {11, 2, 33, 4, 5}
print(set7)

print(set6.union(set7))  # union of sets

print(set6.intersection(set7))  # intersection of sets

print(set6.difference(set7))  # difference()

print(set6.symmetric_difference(set7))  # symmetric difference :  union - intersection

# symmetric_difference_update() : output of symmetric difference is saved in set6
#   this method not returns anything
print(set6.symmetric_difference_update(set7))
print(set6)

# + : not supported (can't concatenate two sets)


#   mutability of sets
# insert operation
set8 = {1, 2, 3}
set8.add(4)
print(set8)

# iterable : traversable i.e list
# update() : same as extend() which is in list
# can be done by tuple but we use list always
#   update adds elements in set which are iterable(in form of list oor tuple)

set8.update([11, 22, 33, 44, 55])
print(set8)

set8.update({10, 20, 30})
print(set8)

# subset:
#   set is subset of itself therefore not possible
# set9 = {1,2,3,{5,6}}
# print(set9)

# removing
set10 = {1, 2, 3, 4, 5}

#   discard(): if value not present will not show any error
set10.discard(10)
print(set10)

#   remove() : if value not present it will give error
set10.remove(4)
print(set10)

#   clear() : removes all elements
set10.clear()
print(set10)

del set10  # del : delete structure
# print(set10)


# operations on set using operators
set11 = {1, 2, 3, 4, 5}
set12 = {1, 2, 3, 7, 8}

#   union : |
print(set11 | set12)

# intersection : &
print(set11 & set12)

# difference : -
print(set11 - set12)
print(set12 - set11)

# symmetric difference : ^
print(set11 ^ set12)
