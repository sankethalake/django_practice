# range function and for loop
# range(start, stop, step)

box = range(1, 5)        # same as:       box = range(1,5,1)
print(type(box))

# for element in container:

for element in box:
    print(element)

# Assignment

table = range(9, 91, 9)

for element in table:
    print(element)

city = ["pune", "Mumbai"]
for element in city:
    print(element)

string = "python"
for x in string:
    print(x)

# -------------------------------------------------------------------------------------------------------
table1 = range(1, 91)

for element in table1:
    if element % 9 == 0:
        print(element)

# -------------------------------------------------------------------------------------------------------
table2 = range(1, 11)

for element in table2:
    print(element * 9)
