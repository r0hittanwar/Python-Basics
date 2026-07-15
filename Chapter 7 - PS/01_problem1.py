# Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter no whose table you want to print: "))

# for i in range(n, n*10 + 1, n):
#     print(i)

# OR (second way)

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")