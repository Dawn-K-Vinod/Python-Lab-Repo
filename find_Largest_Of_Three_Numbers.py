"""
Author: Dawn K Vinod
Date: 25-10-2024
Description: Python program to find the largest of three numbers.
"""
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>num2 and num1>num3:
    print(num1,"is largest.")
elif num2>num3:
    print(num2,"is greatest")
else:
    print(num3,"is greatest")
