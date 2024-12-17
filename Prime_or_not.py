n=int(input("Enter a number:"))
for num in range(2, n): #taking the numbers from 2 to n one-by-one (to check if it is prime or not)
    for i in range(2, num): #for-else to check whether the number in the current iteration is prime or not.
        if num%i==0:
            break
    else: # else part in for-loop works only if the for-loop completes all the iterations in it, without breaking in between.
        # If the for-loop executes any `break` statements within the loop then the else part do not work.
        print(num, end=" ")
