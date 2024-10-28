"""
Author: Dawn K Vinod
Date: 25-10-2024
Description: Python program to convert temperature values back and forth between Celsius and Fahrenheit.
"""
temperature=int(input("Enter temperature:"))
scale =input("Is this in Celsius or Fahrenheit? (Type C or F)")

if scale =='C':
    fahrenheit = (9/5*temperature)+32
    print(temperature,"Celsius is",fahrenheit,"Fahrenheit")
elif scale =='F':
    celsius = 5/9*(temperature-32)
    print(temperature,"Fahrenheit is",celsius,"Celsius")
else:
    print("Invalid temperature code.")


"""
def C_to_F():
    F=(temp*9/5) + 32

def F_to_C():
    C=(temp-32)*5/9
    
def K_to_C():
    C= temp-273.15
    
def C_to_K():
    K= temp + 273.15
    
def F_to_K():
    K= ((temp-32)*5/9) +273.15
    
def K_to_F():
    F=((temp-273.15)*9/5) + 32
    
    
while True:
    print("Temperature Scale Conversion")
    print(" ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Celsius to Kelvin")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    
    temp=int(input("Enter the temperature:"))
    conv=input("Enter any conversions from the given menu:")
    if conv=='1':
        C_to_F(temp)
    if conv=='2':
        F_to_C(temp)
    if conv=='3':
        K_to_C(temp)
"""