# for with else
# print :
# 4
# 5
# 6
# 7
# 8
# END
for number in range(4, 9):
    print(number)
else:
    print("end")

# ----------------------------------------------------------------------------
box = range(4, 10)

for element in box:
    if element > 8:
        print("END")
    else:
        print(element)

# ----------------------------------------------------------------------------

num = 4
while num < 9:
    print(num)
    num += 1
    if num == 9:
        print("end")
