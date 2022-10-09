"""
CP1404/CP5632 - Practical 4
Subject Reader
This program reads from a data and prints them.
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def display_data(data):
    """Iterate each list inside a list and display each list in a formatted string"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    # added empty subject list to pass into
    subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        # this line will append each parts as a list
        subjects.append([parts[0], parts[1], parts[2]])
    input_file.close()
    return subjects


main()
