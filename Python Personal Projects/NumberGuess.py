import random
import time

print("\nWelcome to the Number Guesser!")

run = True #whether the program is running or not
while run:
    print("Set number constraints: ")
    min = int(input("Min: "))
    max = int(input("Max: "))
    if min > max:
        print("Maximum must be greater than the minimum.")
    else:
        print("\nGenerating random number...")
        time.sleep(1)
        rand = random.randint(min, max)
        
        guess = None #None represents null value
        numGuesses = 1 #Number of guesses
        while guess != rand:
            guess = int(input("Take a guess at the mystery number! "))
            if guess < rand:
                print("Higher!")
                numGuesses += 1
            elif guess > rand:
                print("Lower!")
                numGuesses += 1
            else:
                print(f"You found the mystery number in {numGuesses} guesses!")
    runInput = input("Do you wish to play again? (y/n)")
    if runInput.lower() == "n":
        run = False
        print("\nGame finished!\n")
    elif runInput.lower() != "y":
        print("Not a valid response. Restarting game.")
    