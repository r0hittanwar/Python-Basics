#  Write a program which finds out whether a given name is present in a list or not.

list = ["rohit", "nikhil" , "kartik", "naman", "kuldeep", "tushar"]

name = input("Enter name you want to check :")

if(name in list):
    print("Yes! name is present in list")

else:
    print("Name is not present in list")