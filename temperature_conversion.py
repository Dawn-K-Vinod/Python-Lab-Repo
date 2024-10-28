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
