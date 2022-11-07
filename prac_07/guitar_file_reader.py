"""
CP1404/CP5632 - Practical 7
Guitar File Reader
This program opens and reads guitars csv file
Estimate: 100 minutes
Actual:       minutes
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
