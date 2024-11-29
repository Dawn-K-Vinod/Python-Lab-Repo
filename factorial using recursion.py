"""
Author: Dawn K Vinod
Date: 29-11-2024
Description: Program to find the factorial of a number using Recursion.
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

number=abs(int(input("Enter the number:")))
print(f"The factorial of number {number} is: {factorial(number)}")
