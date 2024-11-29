"""
Author: Dawn K Vinod
Date: 29-11-2024
Description: Recursive function to add two positive numbers.
"""
def add_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_numbers(num1+1,num2-1)

number1 = abs(int(input("Enter first number:")))
number2 = abs(int(input("Enter second number:")))
print(f"Sum of {number1} and {number2} is: {add_numbers(number1,number2)}")
