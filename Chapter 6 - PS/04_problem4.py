#  Write a program to find whether a given username contains less than 10 characters or not. 

user_name = input("Enter username :")

if(len(user_name) < 10 ):
    print("Less than 10 characters")

elif(len(user_name) == 10):
    print("Equal to 10 characters")

else:
    print("More than 10 characters")