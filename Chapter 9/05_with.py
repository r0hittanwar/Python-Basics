# f = open("file.txt")
# print(f.read())
# f.close 

# The same can be written using with statement like this
with open("file.txt") as f:
    print(f.read())

# So you don't have to close the file explicitly