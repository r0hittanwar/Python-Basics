class Employee:
    name = "Rohit"
    salary = 250000
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and Salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")

#     def language(self);
#         print(f"The name is {self.name} ans he is good in {self.language}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and salary is {self.salary}")

a = Employee()
b = Programmer()


print(a.company, b.company)
b.showLanguage()