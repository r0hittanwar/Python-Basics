# Write a class “Calculator” capable of finding square, cube and square root of a number. 

class Calculator:

    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"Square is {self.n*self.n}")
    
    def cube(self):
         print(f"Cube root is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"Square root is {self.n**1/2}")

sol = Calculator(4)
# sol.square()
Calculator.square(sol)
sol.cube()
sol.square_root()