# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

with open("poems.txt") as f:
    text = f.read()

# print(text)

if("twinkle" in text):
    print("The word twinkle is present in content")

else:
    print("The word twinkle is not present in content")
