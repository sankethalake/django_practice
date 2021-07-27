
try:
    li1 = [1,2,3,4,5]
    print(li1[10])

except IndexError as e:
    print(e)

# in python it is IndexError
#   in java ArrayIndexOutOfBound
# ##########################################################
try:
    li2 = (1,2,3,4,5)
    print(li2[10])

except IndexError as e:
    print(e)