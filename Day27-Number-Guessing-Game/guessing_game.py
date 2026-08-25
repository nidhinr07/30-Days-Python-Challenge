import random

def choose_difficulty():

    print("\n===== Choose Difficulty =====")

    print("1. Easy   - 10 attempts")
    print("2. Medium - 7 attempts")
    print("3. Hard   - 5 attempts")

    while True:

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:

                return 10, 10

            elif choice == 2:

                return 7, 20

            elif choice == 3:

                return 5, 30

            else:

                print("Please choose 1, 2, or 3.")

        except ValueError:

            print("Please enter a valid number.")


def play_game():

    attempts, starting_score = choose_difficulty()

    number = random.randint(1, 100)

    score = starting_score

    print("\n===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts.")

    while attempts > 0:

        try:

            guess = int(input("\nEnter your guess: "))

        except ValueError:

            print("Please enter a valid number.")

            continue

        if guess < 1 or guess > 100:

            print("Please enter a number between 1 and 100.")

            continue

        if guess == number:

            print("\n🎉 Congratulations!")
            print("You guessed the correct number.")
            print(f"Your score: {score}")

            return

        elif guess < number:

            print("Too low! Try a higher number.")

        else:

            print("Too high! Try a lower number.")

        attempts -= 1
        score = max(0, score - 2)

        if attempts > 0:

            print(f"Attempts remaining: {attempts}")

    print("\nGame Over!")
    print(f"The correct number was {number}.")
    print(f"Your final score: {score}")


def main():

    print("🎮 Welcome to the Number Guessing Game!")

    while True:

        play_game()

        while True:

            again = input("\nDo you want to play again? (y/n): ").lower()

            if again == "y":

                break

            elif again == "n":

                print("Thanks for playing! 👋")

                return

            else:

                print("Please enter y or n.")


main()
