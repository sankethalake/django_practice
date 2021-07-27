# dictionary : mutable, unordered
#       python is: interpreted language

dic1 = {}
print(type(dic1))
print(dic1)

# form of dictionary: {key : value}
dic2 = {1: "python"}
print(dic2)

# key in form of float : can be done, not recommended
dic3 = {1.5: "java"}
print(dic3)

#  key can be string
dic4 = {"key": 100}
print(dic4)

# key and value can be of any class(datatype)
dic5 = {1: "value", "key": 2}
print(dic5)

# two keys can have same value
dic6 ={1: "value", 2: "value"}
print(dic6)

# if same key have different value, latest value is taken
dic7 = {10: "value1", 10: "value2"}
print(dic7)

# Access value using key
dic8 = {"one": "value1", "two": "value2"}
print(dic8["two"])

# list as value inside dictionary
dic9 = {"one":[11,22,33,44], "two": 98}
print(dic9)

print(dic9["one"][1]) #accessing value which is inside list using key and index

# values as tuple inside dictionary
dic10 = {1: (1,2,3,4,5),3:76}

print(dic10[1][4])# accessing value which is inside tuple using key and index

# key as tuple inside inside dictionary (value can be tuple or list)
dic11 = {(1) : [1,2,3,4,5]}
print(dic11[1][1])

# key as a list
# dic12 = {[1] : [1,2,3,4,5]}       # error : list is unhashable
# print(dic12[1][1])
# unhashable : we can modify value of list
#   keys should be hashable i.e. cannot be altered

# dictionary in dictionary
#   internal dictionary is part of value of outer dictionary
dicNew3 = {10: [1,2,3,4,5], 20:{"key": "value"}}
print(dicNew3[20])
print(dicNew3[20]["key"])


# adding key-value pair to dictionary
dicAdd = {1: 20, 2: 30}
dicAdd[3] = 40
print(dicAdd)

# alter value of given key
dicAdd[1] = 200
print(dicAdd)

# update : update() can be used to alter values of keys
dicAdd.update({4:400})
print(dicAdd)
#   more then one value can be updated using update()
dicAdd.update({2:200, 6:600,7:700})
print(dicAdd)
#   new key value pair can be added using update
dicAdd.update({80: 555})
print(dicAdd)

# remove
dicRemove = {1:10, 2:20, 3:30, 4:40, 5:50}
#   pop() with key is used.....empty pop() can't be used in dictionary
dicRemove.pop(4)
print(dicRemove)

#   popitem() : it removes last added key-value pair from python 3.7
#               before it removed any pair randomly
dicRemove.popitem()
print(dicRemove)

# clear() : to clear all key value pair present in dictionary
dicRemove.clear()
print(dicRemove)

# del : it is keyword used to delete the structure
del dicRemove
# print(dicRemove)


# key , values

dicNewest = {1:10, 2:20, 3:30}
#   get() : it takes key as parameter and gives value of that key
print(dicNewest.get(3))

#   keys() : it gives all the keys of dictionary
print(dicNewest.keys())

#   values() : it gives all the values of dictionary
print(dicNewest.values())