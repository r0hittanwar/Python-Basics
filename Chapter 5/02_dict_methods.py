marks = {
    "Maths" : 92,
    "Chem" : 95,
    "Physics" : 64,
    "Music" : 92,
    "English" : 84,
    0 : "Naman"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Maths" : 95})  #because dictionaries are mutable
# marks.update({"Maths" : 95, "Physical" : 74})    #it can also add or update new value in last
# print(marks)

# print(marks.get("Music"))  #if music doesn't exist then it will give none and another line will execute
# print(marks["Music"])     #if music doesn't exist then it will give error and another line will not execute

newDict = marks.fromkeys(marks, 100)
print(newDict)