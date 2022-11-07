"""
CP1404/CP5632 - Practical 6
Guitar
Guitar class
Estimate: 100 minutes
Actual:    10 minutes
"""


class Guitar:

    def __init__(self, name, year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"Guitar: {self.name}, Model Year: {self.year}, Cost: ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year
