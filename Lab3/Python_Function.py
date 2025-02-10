import math
import itertools
import random

# Task 1: Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Task 2: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3: Solve the chickens and rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

# Task 4: Filter prime numbers from a list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

# Task 5: Print all permutations of a string
def string_permutations(string):
    return [''.join(p) for p in itertools.permutations(string)]

# Task 6: Reverse words in a sentence
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Task 7: Check if a list contains 3 next to 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8: Check if a list contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Task 9: Compute the volume of a sphere given its radius
def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# Task 10: Get unique elements from a list
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Task 11: Check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Task 12: Print a histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# Task 13: Guess the number game
def guess_number_game():
    name = input("Hello! What is your name? ")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Take a guess. "))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

# Task 14: Import functions into another file (create a Python file)
if __name__ == "__main__":
    print("Testing functions:")
    print(f"100 grams to ounces: {grams_to_ounces(100)}")
    print(f"100°F to Celsius: {fahrenheit_to_celsius(100)}")
    print(f"Chickens and rabbits: {solve(35, 94)}")
    print(f"Prime numbers from list: {filter_prime([2, 3, 4, 5, 10, 17, 19])}")
    print(f"Permutations of 'abc': {string_permutations('abc')}")
    print(f"Reversed sentence: {reverse_words('We are ready')}")
    print(f"Has 33? {has_33([1, 3, 3])}")
    print(f"Spy game? {spy_game([1, 0, 2, 4, 0, 5, 7])}")
    print(f"Volume of sphere (radius=3): {sphere_volume(3)}")
    print(f"Unique elements: {unique_elements([1, 2, 2, 3, 4, 4, 5])}")
    print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
    print("Histogram of [4, 9, 7]:")
    histogram([4, 9, 7])
    
    # Uncomment below line to play the game
    # guess_number_game()
