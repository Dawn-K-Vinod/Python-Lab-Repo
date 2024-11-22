"""
Author: Dawn K Vinod
Date: 22-11-2024
Description: Print different star patterns using nested loop.
"""
print("Increasing triangle:")
for row in range(1,6):
    for j in range(row):
        print("*",end=" ")
    print(" ")


print("\nDecreasing Triangle:")
for row in range(5,0,-1):
    for j in range(row):
        print("*",end=" ")
    print(" ")


print("\nHill Pattern:")
for row in range(1,6):
    for space in range(5-row):
        print(" ",end=" ")
    for star in range((row*2)-1):
        print("*",end=" ")
    print()

print("\nReverse Hill Pattern:")
for row in range(5,0,-1):
    for space in range(5-row):
        print(" ",end=" ")
    for star in range((row*2)-1):
        print("*",end=" ")
    print()