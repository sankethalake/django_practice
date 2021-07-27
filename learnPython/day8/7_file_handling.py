# files ->
#   modes : read, write, append, create

# open file
file = open("FileHandle.txt", "r")
for each in file:
    print(each)

# read() mode:

file = open("FileHandle.txt", "r")
print(file.read())  # reads all data of file

# print(file.readline())           # reads first line of line           # we commented this lines as they will not give
# output as pointer is at end
# print(file.readlines())          # reads all lines as iterable

# read()  character-wise
file = open("FileHandle.txt", "r")
print(file.read(5))  # read first five characters

print(file.readline(3))  # will at least read one line
file.close()

# create file
file = open("FileHandle.txt", "w")
file.write("this is write mode")
file.write("writing in specific file")
file.close()

#     append() mode
file = open("FileHandle.txt", "a")
file.write("this will append\n add a line")
file.close()

# with()        : when outside with file is automatically closed
with open("FileHandle.txt") as file:
    data = file.read()
    # file.close()                  # no need to write this line
# performing task with data


# split() function: it will split string into words using delimiter string
#   delimiter string by default is whitespace
with open("FileHandle.txt") as file:
    data1 = file.readlines()
    for line in data:
        word = line.split()  # split("@") if we want to split from @ everytime
        print(word)
