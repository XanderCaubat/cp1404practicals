"""
CP1404/CP5632 - Practical 9
Silver Taxi Test
This program test the my_silver_taxi object with Taxi class
Estimate: 2 minutes
Actual:   2 minutes
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    initial_service_car = SilverServiceTaxi("Mustang", 100, 2)
    initial_service_car.drive(18)
    print(initial_service_car)

    # # Additional testing of SilverServiceTaxi class
    # expensive_service_car = SilverServiceTaxi("Hummer", 200, 4)
    # affordable_service_taxi = SilverServiceTaxi("Journey", 100, 2)
    # expensive_service_car.drive(100)
    # print(expensive_service_car)
    # affordable_service_taxi.drive(70)
    # print(affordable_service_taxi)


main()
