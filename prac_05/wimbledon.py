"""
CP1404/CP5632 - Practical 5
Wimbledon
This program read the wimbledon csv file, process the data and display processed information
Estimate: 200 minutes
Actual:   minutes
"""


def main():
    with open('../prac_05/wimbledon.csv', 'r', encoding="utf-8-sig") as in_file:
        lines = [line.strip() for line in in_file.readlines()]
        winners = set(lines)
        print(winners)
        print(len(winners))


main()
