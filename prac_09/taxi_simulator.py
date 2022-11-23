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
            try:
                number_choice = int(input(">>> "))
                current_taxi = taxis[number_choice]
            except IndexError:
                print("Invalid choice")
            except ValueError:
                print("Invalid input")
        elif choice == 'D':
            pass
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
