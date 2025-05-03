# Dice Roller Simulator with a Twist
import random

def roll_dice():
    print("🎲 Welcome to the Dice Roller Simulator with a Twist!")
    
    while True:
        input("Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!")

        if dice == 1:
            print("💀 Oh no! You rolled a 1. You lose!")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == 'y':
                continue
            else:
                print("Thanks for playing! 👋")
                break
        else:
            roll_again = input("You survived! Roll again? (y/n): ").lower()
            if roll_again != 'y':
                print("Thanks for playing! 👋")
                break
roll_dice()