"""
CP1404/CP5632 - Practical
Used Cars
This program stores user's emails and name in a dictionary.
Estimate: 100 minutes
Actual:   30 minutes
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car.name)
    limo = Car(100)
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo.name)
    print(limo.display())


main()
