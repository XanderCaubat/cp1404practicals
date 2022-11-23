"""
CP1404/CP5632 - Practical 9
Taxi Simulator
This program uses Taxi and SilverServiceTaxi classes
Estimate: 30 minutes
Actual:
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "Let's drive!\nq)uit, c)hoose, d)rive"


def main():
    current_taxi = None
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            display_taxis(taxis)
            number_choice = int(input(">>> "))
            get_valid_number_choice(number_choice, taxis)
        elif choice == 'D':
            pass
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()


def get_valid_number_choice(number_choice, taxis):
    try:
        current_taxi = taxis[number_choice]
    except IndexError:
        print("Invalid choice")
    except ValueError:
        print("Invalid input")


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
