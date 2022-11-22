"""
CP1404/CP5632 - Practical 9
Unreliable Car Class
Estimate: 15 minutes
Actual:    minutes
"""

from prac_09.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel):
        """Initialised UnreliableCar class"""
        super().__init__(name, fuel)

    def __str__(self):
        return f"{super().__str__()}"
