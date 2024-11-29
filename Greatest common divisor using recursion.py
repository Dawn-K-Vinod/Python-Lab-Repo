"""
Author: Dawn K Vinod
Date: 29-11-2024
Description: Recursive function to find the greatest common divisor of two positive numbers.
Euclidean Algorithm for Greatest Common Divisor (GCD)
"""
def greatest_common_divisor(num1,num2):
    if num2==0:
        return num1
    else:
        num3=num1%num2
        num1=num2
        num2=num3
        return greatest_common_divisor(num1,num2)


number1=abs(int(input("Enter first number:")))
number2=abs(int(input("Enter second number:")))
print(f"The Greatest Common Divisor of {number1} and {number2} is: {greatest_common_divisor(number1,number2)}")
