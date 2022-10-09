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
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        picks = []
        for j in range(RANDOM_NUMBERS):
            random_number = random.randint(MIN, MAX)
            while random_number in picks:
                random_number = random.randint(MIN, MAX)
            picks.append(random_number)
        print(random_number, end=' ')


main()
