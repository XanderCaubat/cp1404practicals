"""
CP1404/CP5632 - Practical 6
Guitar
This program uses Guitar class as an example
Estimate: 100 minutes
Actual:    minutes
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def display(self):
        return f"{self.name} ({self.year}) : ${self.cost}"
