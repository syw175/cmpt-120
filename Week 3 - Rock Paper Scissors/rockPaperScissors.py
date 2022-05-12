# CMPT120
# Title: Rock Paper Scissors Game
# Name: Steven Wong
# Date: January 31, 2022

import random

# Greet User
print("Hello!")

# Ask the user if they want to play RPS until a valid input is received
while 1:
    gameStart = input("Would you like to play "
                      "Rock, Paper, Scissors? (Yes or No)\n").lower().strip("!.? ")
    if gameStart in ["yes", "yeah", "sure"]:
        print("Good luck and have fun!")
        break
    elif gameStart in ["no", "nope", "nah"]:
        print("Okay fine. Bye!")
        quit()
    else:
        print("That is not a valid input, please try again.")

# Rock paper scissors game
for i in range(3):
    gameOptions = ["rock", "paper", "scissors"]
    user_Pick = input("Your Pick! Rock, Paper, or Scissors?\n").strip("?.! ").lower()
    computer_Pick = random.choice(gameOptions)
    print("You picked", user_Pick)
    print("Computer picked", computer_Pick)

    if user_Pick == computer_Pick:
        print("It's a tie, nobody won!")
    elif user_Pick == "rock":
        if computer_Pick == ("scissors"):
            print("You won!")
        else:
            print("You lost!")
    elif user_Pick == "scissors":
        if computer_Pick == ("paper"):
            print("You won!")
        else:
            print("You lost!")
    elif user_Pick == ("paper"):
        if computer_Pick == ("rock"):
            print("You won!")
        else:
            print("You lost!")
    else:
        print(user_Pick, "is not a valid input. Please try again...")


# This line has exactly 100 characters (including the period), use it to keep each line under limit.