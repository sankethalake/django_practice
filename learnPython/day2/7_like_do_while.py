# trying to write like do while loop of java
#   python does not have a do while loop

element = 1
condition = bool(1)

while condition:
    print(element)
    element += 1

    if element > 3:
        condition = bool(0)

# ---------------------------------------------
num = 1

while True:
    print(num)
    num = num + 1
    if num > 1:
        break
