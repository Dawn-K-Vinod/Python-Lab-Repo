"""
Author: Dawn K Vinod
Date: 25-10-2024
Description: Python program to calculate the sum of digits of a given number.
"""
num = int(input("Enter a number:"))
digit_sum = 0
while num>0:
    remainder = num % 10
    digit_sum += remainder
    num = num//10
print("Sum of digits of a given number:",digit_sum)
