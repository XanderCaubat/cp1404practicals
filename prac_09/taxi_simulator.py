"""
CP1404/CP5632 - Practical 9
Taxi Simulator
This program uses Taxi and SilverServiceTaxi classes
Estimate: 30 minutes
Actual:
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"


def main():
    current_taxi = None
    total_cost = 0
    print("Let's drive!")
    display_menu()
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu_choice = input(">>> ").upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            print("Taxis available:")
            display_taxis(taxis)
            number_choice = int(input("Choose Taxi: "))
            try:
                current_taxi = taxis[number_choice]
                display_current_cost(total_cost)
                display_menu()
            except IndexError:
                print("Invalid taxi choice.")
                display_current_cost(total_cost)
                display_menu()
            except ValueError:
                print("Invalid input.")
                display_current_cost(total_cost)
                display_taxis(total_cost)
        elif menu_choice == 'D':
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                taxi_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${taxi_fare:.2f}")
                total_cost += taxi_fare
                display_current_cost(total_cost)
            else:
                print("You need to choose a taxi before you can drive.")
                display_current_cost(total_cost)
                display_menu()
        else:
            print("Invalid option.")
            display_current_cost(total_cost)
            display_menu()
        menu_choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now: ")
    print(display_taxis(taxis))


def display_menu():
    print(MENU)


def display_current_cost(total_cost):
    print(f"Bill to date: ${total_cost:.2f}")


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
