#  Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt", "r") as f:
    word = f.read()

if("Python" in word):
    print("Python exists in the file")

else:
    print("Python doesn't exists in the file")