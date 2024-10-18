"""
Author: Dawn K Vinod
Date: 18-10-2024
Description: Python program that uses functions from the math module
to perform the following operations on a number provided by the user.
"""
import math

num = int(input("Enter a number:"))
print("Square root of" , str(num) + ":", math.sqrt(num))
print("Factorial of" , str(num) + ":", math.factorial(num))
print(num,"raised to power 2:", math.pow(num,2))
