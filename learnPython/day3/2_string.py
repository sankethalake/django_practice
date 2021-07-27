# String

# string can be written in three types
name = 'Tanmay'  # within single quotes
name2 = "Nishant"  # within double quotes
# within triple quotes  :   multi line string
name3 = '''
R
A
J
'''
print(name)  # Tanmay
print(name2)  # Nishant
print(name3)  # o/p:                               you will get this type of output for this
# R
# A
# J
#


# use of index in string:   index starts with 0
name4 = "ABCD"
print(name4[2])

# index in multi line string: here it also count the enter we used to go to next line
print(name3[0])  # (outputs)
print(name3[1])  # R
print(name3[2])  #
print(name3[3])  # A
print(name3[4])  #
print(name3[5])  # J
print(name3[6])  #

# negative index: it is used to save sources and reduce traversal time if we start from end
#   starts with -1 i.e -1 denotes last character
name = "Niraj"
print(name[-1])  # j

# slice : similar to range
#   [start : stop : step]
name_slice = "ABCDEFG"
print(name_slice[0:])  # ABCDEFG
print(name_slice[0:5])  # ABCDE
print(name_slice[::2])  # ACEG
print(name_slice[0:-2])  # ABCDE
print(name_slice[0:-2:2])  # ACE

# are memory block of each character next to one another according to their index:  NO
alpha = "ABCD"

print(id(alpha[0]))  # id's are not in any order
print(id(alpha[1]))
print(id(alpha[2]))
print(id(alpha[3]))

beta = "BC"  # all B have same id irrespective of where it is used
tiger = "NJJAUXBAKDY"
print(id(alpha[1]))
print(id(beta[0]))
print(id(tiger[6]))

# use of format() in different ways
name = "Kiran"
lname = "Chopde"
id = 1

#   without format()
print("name is ", name, "lname is ", lname, "with id ", id)
#   with format()
print("name is {0} lname is {1} with id {2}".format(name, lname, id))
print("name is {1} lname is {0} with id {2}".format(name, lname, id))
print("name is {a} lname is {b} with id {c}".format(a=name, b=lname, c=id))
