# Write a function that takes a list and returns even numbers only.

list = [12, 54, 13, 56, 89, 47]

def checkEven(numbers):
    even_list = []
    for num in list:
        if (num % 2 == 0):
            even_list.append(num)
    
    return even_list

ans = checkEven(list)
print(ans)