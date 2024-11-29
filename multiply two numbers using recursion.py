"""
Author: Dawn K Vinod
Date: 29-11-2024
Description: Recursive function to multiply two positive numbers
"""
def multiply_numbers(num1,num2):
    if num2>num1:
        num1,num2 = num2,num1
    if num2==1:
        return num1
    else:
        return num1+multiply_numbers(num1,num2-1)

number1 = abs(int(input("Enter first number:")))
number2 = abs(int(input("Enter second number:")))
print(f"Product of {number1} and {number2} is: {multiply_numbers(number1,number2)}")