"""
Author: Dawn K Vinod
Date: 19-10-2024
Description: Create, concatenate, and print a string and access a sub-string from a given string.
"""

first_name=input("Enter your first name:")
last_name=input("Enter your last name:")

full_name=first_name + " " + last_name
print(full_name)

#length of first name
len_firstname=len(first_name)

#Extracting last name from full name
print(full_name[len_firstname+1:])

#Extracting first name from full name
print(full_name[:len_firstname])
