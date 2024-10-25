"""
Author: Dawn K Vinod
Date: 25-10-2024
Description: Python program to check whether the given number is an armstrong number.
"""
num = int(input("Enter a number:"))
input_number=num
digit_cube_sum = 0
while num>0:
    remainder = num % 10
    digit_cube_sum += remainder**3
    num = num//10
if digit_cube_sum == input_number:
    print(input_number,"is an armstrong number.")
else:
    print(input_number,"is not an armstrong number.")