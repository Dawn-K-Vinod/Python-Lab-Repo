"""
Author: Dawn K Vinod
Date: 19-10-2024
Description: Simple desktop calculator using Python. Only the five basic arithmetic operators.
"""
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

#Addition
print("The sum of num1 and num2 is:",num1+num2)

#Subtraction
print("The difference when num2 is subtracted from num1 is:",num1-num2)

#Multiplication
print("The product of num1 and num2 is:",num1*num2)

#Division
print("The quotient when num1 is divided by num2 is:",num1/num2)

#Modulus
print("The remainder when num1 is divided by num2 is:",num1%num2)

#Combined Arithmetic Operation
result=(num1+num2)*num3/2
print("The result of (num1+num2)*num3/2 is:",result)
