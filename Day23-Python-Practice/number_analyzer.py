# Day 23 - Number Analyzer


numbers = [10, 25, 8, 42, 15, 30]


def analyze_numbers(numbers):

    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    print("Numbers:", numbers)
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Total:", total)
    print("Average:", average)
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)


analyze_numbers(numbers)
