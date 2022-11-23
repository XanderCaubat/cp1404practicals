"""
CP1404/CP5632 - Practical 9
Taxi Test
This program test the my_taxi object with Taxi class
Estimate: 15 minutes
Actual:   13 minutes
"""

from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi.name, my_taxi.price_per_km)
    print(my_taxi.get_fare())
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi.name, my_taxi.price_per_km)
    print(my_taxi.get_fare())


main()
