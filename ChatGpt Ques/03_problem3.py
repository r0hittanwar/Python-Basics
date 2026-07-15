# Write a function to find missing numbers from a list of 1 to N.

n = int(input("Enter n: "))
nums = [1, 2, 5, 8, 9, 6]

def missing(nums, n):
    missing = []
    for i in range(1, n+1):
        if i not in nums:
            missing.append(i)

    return missing

result = missing(nums, n)
print(result)
        