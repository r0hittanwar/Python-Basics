# Write a function to generate the first N Fibonacci numbers.

n = int(input("Enter number: "))

def fibonacci(n):
    fib_list = []
    a, b = 0, 1

    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b

    return fib_list


result = fibonacci(n)
print(result)

    