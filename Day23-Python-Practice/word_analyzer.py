# Day 23 - Word Analyzer


def analyze_text(text):

    characters = len(text)

    words = len(text.split())

    vowels = 0
    consonants = 0

    for char in text.lower():

        if char.isalpha():

            if char in "aeiou":
                vowels += 1

            else:
                consonants += 1

    reversed_text = text[::-1]

    print("\n----- Word Analyzer -----")

    print("Characters:", characters)
    print("Words:", words)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Reversed:", reversed_text)


text = input("Enter a word or sentence: ")

analyze_text(text)
