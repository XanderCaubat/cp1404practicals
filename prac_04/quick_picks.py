"""
CP1404/CP5632 - Practical 4
Quick Picks
This program ask user how many quick picks they wish to generate.
"""
import random

MIN = 1
MAX = 45
RANDOM_NUMBERS = 6


def main():
    number_of_picks = get_valid_number()
    for i in range(number_of_picks):
        picks = []
        for j in range(RANDOM_NUMBERS):
            random_number = random.randint(MIN, MAX)
            while random_number in picks:
                random_number = random.randint(MIN, MAX)
            picks.append(random_number)
        picks.sort()
        print(" ".join([f"{random_number}" for random_number in picks]))


def get_valid_number():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Invalid number of picks!")
        number_of_picks = int(input("How many quick picks? "))
    return number_of_picks


main()
