"""
CP1404/CP5632 - Practical 6
Guitars
This program stores a list of guitars until they enter a blank name.
Estimate: 100 minutes
Actual:    40 minutes
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = get_year()
        cost = get_cost()
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        display_guitar_added(cost, name, year)
        name = input("Name: ")
    add_to_list(guitars)
    display_guitars(guitars)


def get_cost():
    is_valid = False
    while not is_valid:
        try:
            cost = float(input("Cost: $"))
            is_valid = True
        except ValueError:
            print("Invalid integer!")
    return cost


def get_year():
    is_valid = False
    while not is_valid:
        try:
            year = int(input("Year: "))
            is_valid = True
        except ValueError:
            print("Invalid integer!")
    return year


def add_to_list(guitars):
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


def display_guitars(guitars):
    print("These are my guitars:")
    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year_model}), worth ${guitar.cost:10,.2f}{vintage_string}")


def display_guitar_added(cost, name, year):
    print(f"{name} ({year}) : ${cost:.2f} added.")


main()
