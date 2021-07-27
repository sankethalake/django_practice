# exception handling:
#         Q: can it be compile time as well as runtime

#   as : to give different name
#       why req. to give different name:
#               exception is class in java which provide object in heap memory where we store info about exception
#  in python,     exception is class, we can't print class, so we take a different name
#   as everything is object in python

print("Start")
print("1")
print("2")

try:
    print("3",1/0)
except ZeroDivisionError as e:          # ZeroDivisionError can be replaced with Exception
    print(e)

print("4")
print("5")
print("End")