class Employee:
    language = "Python"  #This is a class attribute
    salary = 1000000

rohit = Employee()
rohit.name = "Rohit Tanwar"     # This is an instance attribute
print(rohit.name, rohit.language, rohit.salary)

shubham = Employee()
shubham.name = "Shubham Mehra"
print(shubham.name, shubham.language, shubham.salary)

# Here name is an instance attribute anguage and salary are class attributes as they directly belongs to the class