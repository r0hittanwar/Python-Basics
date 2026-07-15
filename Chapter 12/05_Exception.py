try:
    a = int(input("Hey, Enter the number: "))       #if we enter an number then the program will work correctly but on an invalid value it will goes to the except block then do what we write but do not get crash
    print(a)
    
except ValueError as v:
    print("Heyyyy")
    print(v) 

except Exception as e:     #but without except block it will be crashed on entering invalid input
    print(e)

print("Thank you")
