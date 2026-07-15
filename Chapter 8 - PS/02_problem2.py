# Write a python program using function to convert Celsius to Fahrenheit.

def convert_temp(cel):
    return cel * (9/5) + 32

cel = float(input("Enter temprature: "))

ans = convert_temp(cel)
print(f"{cel}°C equals to {round(ans)}°F")