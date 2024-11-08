"""
Author: Dawn K Vinod
Date: 08-11-2024
Description: Python program to find the first and the second,largest and smallest numbers
from the given list of numbers.
"""
n=int(input("Enter how many numbers to be inputted:"))
if n==0:
    print("Zero numbers were inputted.")
    exit()
    
num=int(input("Enter number 1:"))
largest=num
smallest=num
second_largest=None
second_smallest=None

for i in range(2,n+1):
    num=int(input(f"Enter number {i}:"))

    if num>largest:
        second_largest=largest
        largest=num
    elif num!=largest and (second_largest is None or num>second_largest):
        second_largest=num

    if num<smallest:
        second_smallest=smallest
        smallest=num
    elif num!=smallest and (second_smallest is None or num<second_smallest):
        second_smallest=num

print(f"Largest is: {largest}")
print(f"Smallest is: {smallest}")

if second_largest is not None:
    print(f"second Largest is: {second_largest}")
    print(f"Second Smallest is: {second_smallest}")
else:
    print("The given number of inputs were less than 2.\nTherefore, there is no second number.")
