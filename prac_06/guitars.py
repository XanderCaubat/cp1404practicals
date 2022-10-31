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
    name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = [name, year, cost]
        guitars.append(guitar)
        display_guitar_added(cost, name, year)
        name = input("Name: ")
    print("These are my guitars:")
    vintage_string = ""
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def display_guitar_added(cost, name, year):
    print(f"{name} ({year}) : ${cost:.2f} added.")


main()
