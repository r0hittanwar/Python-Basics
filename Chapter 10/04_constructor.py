class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, language, salary):    # dunder method autimatically called when object is created
         self.name = name
         self.language = language
         self.salary = salary
         print("i am creating an object")

    def getInfo(self):     # can accept object using any name but we generally uses self
        print((f"The Language is {self.language}. The salary is {self.salary}"))

    @staticmethod      # here as we can see greet does not need self object then we mark greet as static method
    def greet():
            print("Good morning")


harry = Employee("Harry", "JavaScript", 1500000)
harry.name = "Harry"
print(harry.name, harry.language, harry.salary)   
