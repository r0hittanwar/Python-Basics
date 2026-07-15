# Write a recursive function to calculate the sum of first n natural numbers.
n = int(input("Enter n: "))

def sum(n):
    if(n == 1):
        return 1
    return n + sum(n - 1)

ans = sum(n)
print(ans)