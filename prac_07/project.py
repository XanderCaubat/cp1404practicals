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
        return f"{self.name}, start: {self.start_date}, " \
               f"priority {self.priority}, estimate: ${self.cost}, completion: {self.percent}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def __is_complete__(self):
        return self.percent == 100


def run_test():
    project = Project("Build Car Park", "12/09/2021", 2, 600000.0, 100)
    print(project)
    print(project.__is_complete__())


if __name__ == '__main__':
    run_test()
