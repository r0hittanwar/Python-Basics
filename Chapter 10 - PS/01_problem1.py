# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "Microsft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin



r = Programmer("Rohit Tanwar", 1200000, 121102 )
print(r.name, r.pin, r.company, r.salary)
n = Programmer("Naman Jangra", 1000000, 121105 )
print(n.name, n.pin, n.company, n.salary)