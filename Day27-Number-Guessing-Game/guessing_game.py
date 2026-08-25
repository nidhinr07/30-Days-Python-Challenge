# Day 27 - Number Guessing Game
# Commit 2 - Limited Attempts and Hints


import random


number = random.randint(1, 100)

attempts = 7


print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.")


while attempts > 0:

    guess = int(input("Enter your guess: "))

    if guess == number:

        print("🎉 Congratulations!")
        print("You guessed the correct number.")

        break

    elif guess < number:

        print("Too low! Try a higher number.")

    else:

        print("Too high! Try a lower number.")

    attempts -= 1

    if attempts > 0:

        print(f"Attempts remaining: {attempts}")

    else:

        print("\nGame Over!")
        print(f"The correct number was {number}.")
