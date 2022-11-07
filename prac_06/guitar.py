"""
CP1404/CP5632 - Practical 6
Guitar
This program uses Guitar class as an example
Estimate: 100 minutes
Actual:    25 minutes
"""
from datetime import datetime

VINTAGE_AGE = 50
current_date_time = datetime.now()


class Guitar:

    def __init__(self, name="", year_model=0, cost=0):
        self.name = name
        self.year_model = year_model
        self.cost = cost

    def display(self):
        return f"{self.name} ({self.year_model}) : ${self.cost}"

    def get_age(self):
        return current_date_time.year - self.year_model

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year_model < other.year_model
