# importing function from other file
#   syntax: import <fileName>
#   this is not feasible
import Add

# accessing function :
#   fileName.function()
Add.add(10, 20)

###################################################
# always go for from
from Add import sub

sub(10,20)

# import a file which is outside project
# from C:\Users\Dell\PycharmProjects\Sub