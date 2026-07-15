# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class Demo:
    a = 5

o = Demo()
print(o.a)   # prints the class attribute because instance attribute is not present
o.a = 0     # it does not change the class attribute but sets a instance attribute
print(o.a)
print(Demo.a)