"""
CP1404/CP5632 - Practical 9
Unreliable Car Class
Estimate: 15 minutes
Actual:   10 minutes
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialised UnreliableCar class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, {self.reliability}"

    def drive(self, distance):
        random_distance = randint(0, 100)
        if random_distance >= self.reliability:
            distance = 0
        distance_drive = super().drive(distance)
        return distance_drive
