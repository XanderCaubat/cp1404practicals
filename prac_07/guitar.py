"""
CP1404/CP5632 - Practical 6
Guitar
Guitar class
Estimate: 100 minutes
Actual:       minutes
"""


class Guitar:

    def __init__(self, name, year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"Guitar: {self.name}, Model Year: {self.year}, Cost: ${self.cost}"
