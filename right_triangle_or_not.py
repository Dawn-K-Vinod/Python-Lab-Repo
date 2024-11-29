"""
Author: Dawn K Vinod
Date: 29-11-2024
Description: A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether the triangle is a right triangle or not
(Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals
the sum of the squares of the other two sides). Implement using functions.
"""


def right_triangle_or_not(side_1,side_2,side_3):
    sides=[side_1,side_2,side_3]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("The given triangle is a right triangle")
    else:
        print("The given triangle is not a right triangle")

side1=int(input("Enter the length of first side:"))
side2=int(input("Enter the length of second side:"))
side3=int(input("Enter the length of third side:"))
right_triangle_or_not(side1,side2,side3)

