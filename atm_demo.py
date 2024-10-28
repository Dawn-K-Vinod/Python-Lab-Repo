"""
Author: Dawn K Vinod
Date: 28-10-2024
Description: Python program that simulates a simple bank ATM system. The user has an initial balance of $1000.
The ATM should display a menu with options to:
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Exit
"""
balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice==2:
        deposit_money = float(input("Enter the amount to deposit:"))
        balance_amount = balance_amount + deposit_money
        print(f"The deposited amount ${deposit_money} \nThe current balance ${balance_amount}")
    elif choice==3:
        withdraw_money = float(input("Enter the amount to withdraw:"))
        if withdraw_money > balance_amount:
            print("Insufficient Balance!")
        else:
            balance_amount = balance_amount - withdraw_money
            print(f"The withdrawn amount ${withdraw_money} \nThe current balance ${balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid Entry")
