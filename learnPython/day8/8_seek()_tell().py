file = open("TellAndSeek.txt","r")

# where is pointer now? : 0
print(file.tell())
print(file.read())
print(file.tell())
print(file.read())          #   no output for this line as pointer is at end of line

# Reset to pointer 0
print(file.seek(0))
print(file.readline())

print(file.tell())
print(file.close())