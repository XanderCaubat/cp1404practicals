"""
CP1404/CP5632 - Practical 9
Taxi Test
This program test the my_taxi object with Taxi class
Estimate: 15 minutes
Actual:    minutes
"""


class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        if not self.musicians:
            return f"{self.name} needs an instrument"
        return f"{self.name} is playing: {self.musicians[0]}"
