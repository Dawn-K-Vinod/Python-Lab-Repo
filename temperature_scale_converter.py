"""
Author: Dawn K Vinod
Date: 28-10-2024
Description: A Menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
"""

while True:
    print("\n1.\tCelsius to Fahrenheit")
    print("2.\tFahrenheit to Celsius")
    print("3.\tExit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        celsius=float(input("Enter the temperature in Celsius:"))
        fahrenheit=(celsius*9/5) + 32
        print(f"{celsius} Celsius to {fahrenheit} Fahrenheit")

    elif choice==2:
        fahrenheit=float(input("Enter the temperature in Fahrenheit:"))
        celsius=(fahrenheit-32)*5/9
        print(f"{fahrenheit} Fahrenheit to {celsius} Celsius")

    elif choice==3:
        break
    else:
        print("Invalid Entry.")