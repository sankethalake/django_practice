# Methods in String
#   stringName --> Java (camelCase)
#   string_Name --> Python (snake_case)

string_name = "ABCDEFG"
string_name2 = "abc"


# use of upper() and lower()
print(string_name.lower())
print(string_name2.upper())

# use of find(): used to get index of element in string... if not present gives -1
print(string_name.find("a"))
print(string_name.find("A"))


# we have to check what a method does when we use it : it changes the string or return the modified string
#   if a method return a modified string, we have to either print or store it in object
#   this will not do any changes to original string...eg. lower(), upper(), replace()


# use of replace()
string_name.replace("AB","XY")
st = string_name.replace("AB","XY")
print(string_name)                          # ABCDEFG
print(string_name.replace("AB","XY"))       # XYCDEFG
print(st)                                   # XYCDEFG

print("Hello Python".replace("Python","Java"))
string = "Hello Python".replace("Python","Java")
print(string)


