import random

choices = ["rock", "paper", "scissors"]


def get_player_choice():

    while True:

        choice = input(
            "\nChoose rock, paper, scissors or quit: "
        ).lower().strip()

        if choice in choices or choice == "quit":

            return choice

        print("Invalid choice. Please try again.")


def get_result(player_choice, computer_choice):

    if player_choice == computer_choice:

        return "draw"

    if (
        player_choice == "rock"
        and computer_choice == "scissors"
    ) or (
        player_choice == "paper"
        and computer_choice == "rock"
    ) or (
        player_choice == "scissors"
        and computer_choice == "paper"
    ):

        return "player"

    return "computer"


def play_game():

    player_score = 0
    computer_score = 0
    draws = 0
    total_rounds = 0

    print("\n===== Rock Paper Scissors =====")

    while True:

        player_choice = get_player_choice()

        if player_choice == "quit":

            break

        computer_choice = random.choice(choices)

        total_rounds += 1

        print("\nYou chose:", player_choice)
        print("Computer chose:", computer_choice)

        result = get_result(
            player_choice,
            computer_choice
        )

        if result == "draw":

            print("It's a draw!")

            draws += 1

        elif result == "player":

            print("You win! 🎉")

            player_score += 1

        else:

            print("Computer wins!")

            computer_score += 1

        print("\n----- Score -----")

        print("Your wins:", player_score)
        print("Computer wins:", computer_score)
        print("Draws:", draws)

    print("\n===== Final Statistics =====")

    print("Total rounds:", total_rounds)
    print("Your wins:", player_score)
    print("Computer wins:", computer_score)
    print("Draws:", draws)

    if total_rounds > 0:

        win_percentage = (
            player_score / total_rounds
        ) * 100

        print(
            f"Your win percentage: "
            f"{win_percentage:.2f}%"
        )

    else:

        print("No rounds played.")


def main():

    print("🎮 Welcome to Rock Paper Scissors!")

    while True:

        play_game()

        while True:

            replay = input(
                "\nDo you want to play again? (y/n): "
            ).lower().strip()

            if replay == "y":

                break

            elif replay == "n":

                print("Thanks for playing! 👋")

                return

            else:

                print("Please enter y or n.")


main()
