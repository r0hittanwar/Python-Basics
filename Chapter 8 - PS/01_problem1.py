# Write a program using functions to find greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

#using max keyword
# def greatest(a, b, c):
#     return max(a, b, c)

# ans = greatest(a, b, c)
# print(ans)

# using conditionals

def greatest(a, b, c):
    if(a > b and a > c ):
        return a

    elif(b > a and b > c):
       return b

    else:
        return c

ans = greatest(a, b, c)
print(f"Greatest number is: {ans}")   
    