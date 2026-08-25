# Day 27 - Number Guessing Game
# Commit 3 - Score System and Difficulty Levels


import random


def choose_difficulty():

    print("\n===== Choose Difficulty =====")

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter your choice: ")

    if choice == "1":

        return 10, 10

    elif choice == "2":

        return 7, 20

    elif choice == "3":

        return 5, 30

    else:

        print("Invalid choice. Medium difficulty selected.")

        return 7, 20


def play_game():

    attempts, points = choose_difficulty()

    number = random.randint(1, 100)

    print("\n===== Number Guessing Game =====")

    print("I have selected a number between 1 and 100.")

    print(f"You have {attempts} attempts.")

    score = points

    while attempts > 0:

        guess = int(input("\nEnter your guess: "))

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

        score -= 2

        if attempts > 0:

            print(f"Attempts remaining: {attempts}")

        else:

            print("\nGame Over!")

            print(f"The correct number was {number}.")


play_game()
