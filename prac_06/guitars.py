"""
CP1404/CP5632 - Practical 6
Guitars
This program stores a list of guitars until they enter a blank name.
Estimate: 100 minutes
Actual:     minutes
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = [name, year, cost]
    guitars.append(guitar)
    print(f"{name} ({year}) : ${cost:.2f} added.")


main()
