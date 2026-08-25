# Day 27 - Number Guessing Game
# Commit 1 - Basic Guessing Game


import random


number = random.randint(1, 100)


print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")


while True:

    guess = int(input("Enter your guess: "))

    if guess == number:

        print("Congratulations! You guessed the correct number.")

        break

    elif guess < number:

        print("Too low! Try again.")

    else:

        print("Too high! Try again.")
