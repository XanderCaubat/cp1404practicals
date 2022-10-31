"""
CP1404/CP5632 - Practical 6
Guitars
This program stores a list of guitars until they enter a blank name.
Estimate: 100 minutes
Actual:     minutes
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    cost, name, year = get_guitar()
    # add_guitar(cost, guitars, name, year)
    while name != "":
        cost, name, year = get_guitar()
        # add_guitar(cost, guitars, name, year)
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")


def add_guitar(cost, guitars, name, year):
    guitar = [name, year, cost]
    guitars.append(guitar)
    print(f"{name} ({year}) : ${cost:.2f} added.")


def get_guitar():
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return cost, name, year


main()
