# search if the word exist in the file or not.

word = "independent"
with open("new_file.txt") as f:
    content = f.read()

if(word in content):
    print("Found")
else:
    print("Not found")