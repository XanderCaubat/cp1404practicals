"""
CP1404/CP5632 - Practical 9
Unreliable Car Test
This program test the my_unreliable_car object with Car class
Estimate: 15 minutes
Actual:   17 minutes
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    my_unreliable_car = UnreliableCar("Ford 1991", 100, 23)
    my_new_bought_car = UnreliableCar("Lotus 2022", 100, 90)
    my_unreliable_car.drive(100)
    print(my_unreliable_car)
    for i in range(1, 15):
        print(f"Distance {i} km")
        print(f"{my_unreliable_car.name} drove {my_unreliable_car.drive(i)}km")
        print(f"{my_new_bought_car.name} drove {my_new_bought_car.drive(i)}km")

    print(my_unreliable_car)
    print(my_new_bought_car)


main()
