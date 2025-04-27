import random          #Importing the random module to generate random numbers
# This is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.
# The game provides feedback on whether the guess is too high or too low and counts the number of attempts until the user guesses correctly.
def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 to 100.")

    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        try:
            # Get the user's guess
            guess = int(input("Make a guess: "))
            attempts += 1  # Count each guess

            # Compare the guess to the secret number
            if guess < secret_number:
                print("Too low. Try again!")
            elif guess > secret_number:
                print("Too high. Try again!")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} tries.")
                break  # Exit the loop when guessed correctly

        except ValueError:
            # If user types something that's not a number
            print("⚠️ Please enter a valid number!")

# Start the game
number_guessing_game()
