#  Write a python function to remove a given word from a list ad strip it at the same time.

def remove_word(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n

list = ["Programming", "New", "Raw", "ming"]
ans = remove_word(list, "ming")
print(ans)