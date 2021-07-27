li1 =[1,2,3,4,5] # key
li2 = [10,20,30,40,50] # value

# create dictionary
dic={}
for b1, b2 in zip(li1,li2):
    dic[b1] = b2

print(dic)


key = [1,2,3]
values = [11,22,33]
dictionary = dict(zip(key, values))
print(dictionary)

# ###########################################################
# check if a value is present in dict for eg. 30
dic1 = {1: 10, 2: 20, 3: 30}

flag = False
for value in dic1.values():
    if value == 30:
        flag = True
if flag:
    print("present")
else:
    print("not present")





print(30 in dic1.values())



# #######################################################

# name : value
# lname : value
# clgName : value
# roll : value

dic2 = {"name": "max", "lname": "smith", "clgname": "DYPIEMR", "roll": 28 }

key = input("enter the key : ")
if key in dic2.keys():
    print(dic2[key])
else:
    print("this key is not present")




