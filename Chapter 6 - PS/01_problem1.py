# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter No. 1 :"))
b = int(input("Enter No. 2 :"))
c = int(input("Enter No. 3 :"))
d = int(input("Enter No. 4 :"))

if(a > b and a > c and a > d):
    print("Greatest is :", a)

elif(b > a and b > c and b > d):
    print("Greatest is :", b)

elif(c > a and c > b and c > d):
    print("Greatest is :", c)

elif(d > a and d > b and d > c):
    print("Greatest is :", d)