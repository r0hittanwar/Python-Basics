class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):     # can accept object using any name but we generally uses self
        print((f"The Language is {self.language}. The salary is {self.salary}"))

    @staticmethod      # here as we can see greet does not need self object then we mark greet as static method
    def greet():
            print("Good morning")


harry = Employee()
harry.name = "Harry"
harry.greet()
# harry.language = "JavaScript"
harry.getInfo()    # Automatically converts to Employee.getInfo(harry)
# Employee.getInfo(harry)     # both do the same work

