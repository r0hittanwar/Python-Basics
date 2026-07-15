class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    def __len__(self):
        return len(self.n)
    
n = Number("Rohit")
m = Number(2)

# print(n + m)
# print(n * m)
print(len(n))