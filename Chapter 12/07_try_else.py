try:
    a = int(input("Enter the number: "))  
    print(a)

except Exception as e:
    print(e)

else:   #if the try block runs succcesfully then the else block will also runs.
    print("I am inside Else block")
