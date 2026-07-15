class Employee:
    language = "Python"
    salary = 1200000

harry = Employee()
harry.language = "JavaScript"
print(harry.language, harry.salary)

# Note: Instance attributes, take preference over class attributes during assignment & retrieval.
# So that's why JavaScript will be printed instead of Python. 