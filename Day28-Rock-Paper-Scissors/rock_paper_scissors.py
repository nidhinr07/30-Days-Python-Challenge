# Day 28 - Rock Paper Scissors
# Commit 2 - Score System


import random


choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
draws = 0


while True:

    player_choice = input(
        "\nChoose rock, paper, scissors or quit: "
    ).lower()

    if player_choice == "quit":
        break

    if player_choice not in choices:

        print("Invalid choice. Try again.")

        continue

    computer_choice = random.choice(choices)

    print("\nYou chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:

        print("It's a draw!")

        draws += 1

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

        player_score += 1

    else:

        print("Computer wins!")

        computer_score += 1

    print("\n----- Score -----")

    print("Your score:", player_score)
    print("Computer score:", computer_score)
    print("Draws:", draws)


print("\n===== Final Score =====")

print("Your score:", player_score)
print("Computer score:", computer_score)
print("Draws:", draws)
