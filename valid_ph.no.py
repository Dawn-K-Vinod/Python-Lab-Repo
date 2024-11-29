"""
Author: Dawn K Vinod
Date: 29-11-2024
Description: Program to check whether the given number is a valid mobile number or not using functions.
Every number should contain exactly 10 digits. The first digit should be 7 or 8 or 9.
"""
def check_phone_number_validation(num):
    if len(num)==10 and int(num[0]) in [7,8,9]:
        return True
    else:
        return False

phone_number = input("Enter the phone number:")
validity = check_phone_number_validation(phone_number)

if validity:
    print("The given phone number is valid.")
else:
    print("The given phone number is not valid.")

