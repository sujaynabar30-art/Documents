import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:  
    print("-" * 40)
    print("\n🎮 Welcome to the Number Guessing Game! 🎮")
    print("I am thinking of a number between 1 and 100.")

    # 1. Generate a random whole number between 1 and 100
    secret_number = random.randint(1, 100)
    #print(f"Secret number = {secret_number}") # This is just for testing, you can remove it later!

    # 2. We create a counter variable to keep track of their guesses
    attempts = 0

    while True:
        try:
            guess = int(input("\nTake a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Every time they make a valid guess, we add 1 to their attempts
        attempts += 1

        # 3. The Game Logic (Too high, too low, or just right)
        if guess < secret_number:
            print("Too low! Try going higher.")
        elif guess > secret_number:
            print("Too high! Try going lower.")
        else:
            # If it's not too high and not too low, it must be the exact number!
            print(f"\n🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed my number in {attempts} attempts!")
            print("-" * 40)
            break # End the game loop
    
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break