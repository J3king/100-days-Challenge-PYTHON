# Rock, Paper, Scissors Game
import random 
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")    
else:
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")  
    print(f"Computer chose: {computer_choice}") 
    print(f"You chose: {user_choice}")
    print("Thanks for playing!")