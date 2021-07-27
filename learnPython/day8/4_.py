# rules of try block
#       try -> except(atleast 1)
#       try -> except(can be multiple)
#       try -> finally(max. 1)


# # multiple except blocks for single try block
#
# try:
#     li1 = [1, 2, 3, 4, 5]
#     print(li1[10] / 0)
#
# except ZeroDivisionError as e:
#     print("this is block 1", e)
#
# except Exception as e:
#     print("this is block 2", e)
#
# #   soln: this is block 2 : as first it will try to access li1[10]
# #           and when not found go to except block, and not look for ZeroDivisionError
#
#
# # ############################################################################################
# try:
#     li1 = [1, 2, 3, 4, 5]
#     print(li1[10] / 0)
#
# except Exception as e:
#     print("this is block 2", e)
#
#
# except ZeroDivisionError as e:
#     print("this is block 1", e)
#
# #   error in java, warning in python    warning: to broad class
# #       always go for specific to generic and not generic to specific
#
# # similar example
# try:
#     li1 = [1, 2, 3, 4, 5]
#     print(3 / 0)
#
# except Exception as e:
#     print("this is block 2", e)
#
#
# except IndexError as e:
#     print("this is block 1", e)
#
#
# # #################################################################################
#
# #   nested try blocks
# try:
#     print(3/0)
#
#     try:
#         print(10/0)
#
#     except Exception as e:
#         print("this is inner except block",e)
#
# except ZeroDivisionError as e:
#     print("this is block 1",e)
#
# except Exception as e:
#     print("this is block 2",e)

# ################################################
# try with else block.... if there is no exception it prints else code
# try:
#     print(3/3)
#
# except ZeroDivisionError as e:
#     print("this is block 1",e)
#
# else:
#     print("this is else code")



# try block with except and finally

try:
    print(3/3)

except ZeroDivisionError as e:
    print("this is block 1",e)

finally:
    print("this is finally code")

print("5")



# try block with finally
try:
    print(3/3)

finally:
    print("this is finally block")

print("End")