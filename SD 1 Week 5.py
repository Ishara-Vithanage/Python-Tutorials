print("Exercise o1")
import random

count = 1 # Store the count
while True: 
    rand_num = random.randint(0,10) # Generate random number
    print(f"Number {count} is {rand_num}") # Print the output
    if rand_num == 0: # If random number becomes 0, loop should be stopped
        break
    count += 1
    
    
print("-"*10)
print("Exercise 02")

secret_num = random.randint(1, 100)
count = 1
while True:
    guess = int(input("Guess the number: "))
    if guess > secret_num:
        print("Too high")
        count +=1
    elif guess < secret_num:
        print("Too low")
        count +=1
    elif guess == secret_num:
        print(f"You found the number after {count} attempts")
        break
    else:
        print("Invalid input. Please enter number.")

