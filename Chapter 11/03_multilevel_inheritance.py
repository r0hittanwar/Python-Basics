class Employee:
    name = "Rohit"
    salary = 250000
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and Salary is {self.company}")

class coder(Employee):
    language = "Python"
    def printLanguage(self):
        print(f"Out of all langauges here is your language: {self.language}")

class Programmer(coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name of company is {self.company} and salary is {self.salary}")


a = Programmer()
a.show()
a.printLanguage()
a.showLanguage()