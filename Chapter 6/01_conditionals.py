a = int(input("Enter Age :"))

if(a >= 18):
    print("You are above the age of consent")

elif(a == 0):
    print("0 is not a valid age")

elif(a < 0):
    print("You are entering an invalid age")

else:
    print("You are below the age of consent") 

print("End of program")