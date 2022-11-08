"""
CP1404/CP5632 - Practical 7
Project
project Class
Estimate: 30 minutes
Actual:      minutes
"""


class Project:

    def __init__(self, name, start_date, priority=0, cost=0.00, percent=0.00):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percent = percent

    def __repr__(self):
        return f"{self.name}, starting date: {self.start_date}, " \
               f"priority = {self.priority}, ${self.cost}, {self.percent}%"

    def __lt__(self, other):
        return self.priority < other.priority
