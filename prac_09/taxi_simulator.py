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
    total_cost = 0
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            display_taxis(taxis)
            number_choice = int(input(">>> "))
            try:
                current_taxi = taxis[number_choice]
            except IndexError:
                print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        elif choice == 'D':
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                taxi_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${taxi_fare:.2f}")
                total_cost += taxi_fare
            else:
                print("You need to choose a taxi before you can drive.")
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
