# Day 28 - Rock Paper Scissors
# Commit 1 - Basic Game


import random


choices = ["rock", "paper", "scissors"]


player_choice = input(
    "Choose rock, paper, or scissors: "
).lower()

computer_choice = random.choice(choices)


print("\nYou chose:", player_choice)
print("Computer chose:", computer_choice)


if player_choice == computer_choice:

    print("It's a draw!")

elif (
    player_choice == "rock"
    and computer_choice == "scissors"
) or (
    player_choice == "paper"
    and computer_choice == "rock"
) or (
    player_choice == "scissors"
    and computer_choice == "paper"
):

    print("You win! 🎉")

else:

    print("Computer wins!")
