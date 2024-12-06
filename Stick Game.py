print("Welcome to the Stick Game.")
print("Description: The player to pick the last stick loses the game.")
print("Rules:")
print("This is a two player game.\n16 sticks are on the table.")
print("Each player can picks one set of sticks during his/her turn.")
print("A set contains 1, 2, or 3 sticks.")

remaining_sticks=16
player1=input("Enter the name of Player1: ")
player2=input("Enter the name of Player2: ")

n=1
while True:
    turn = player1 if n%2!=0 else player2
    print(f"Remaining sticks: {remaining_sticks}")
    number_of_sticks_in_the_set=int(input(f"{turn}, pick a set of 1,2 or 3 sticks: "))
    if (remaining_sticks-number_of_sticks_in_the_set)<0:
        print("\nInsufficient sticks. Please Try Again.")
        continue
    elif remaining_sticks==number_of_sticks_in_the_set:
        print(f"\n{turn} Lost the game.")
        break
    else:
        remaining_sticks -= number_of_sticks_in_the_set
    n+=1
