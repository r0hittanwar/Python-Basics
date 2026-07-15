# Write a python function which inch_to_cms inches to cms.

def inch_to_cm(inches):
    return inches * 2.54

inches = int(input("Enter inches: "))
print(f"{inches} inches = {inch_to_cm(inches)} Cm")