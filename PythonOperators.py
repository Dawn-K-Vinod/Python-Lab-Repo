"""
Author: Dawn K Vinod
Date: 18-10-2024
Description: Python program that demonstrates the usage of arithmetic, comparison,
and logical operators. Perform a few operations and print the results.
"""
num1 = int(input("Enter the first Number:"))
num2 = int(input("Enter the second Number:"))

sum = num1 + num2
division = num1 / num2
is_greater = num1 > num2
is_equal = num1 == num2

print("Sum:",sum,",Division:",division)
print("Is num1 greater than num2?",is_greater)
print("Are num1 and num2 equal?",is_equal)

print("Logical AND:",num1>0 and num2>0)
print("Logical OR:",num1>0 or num2>0)