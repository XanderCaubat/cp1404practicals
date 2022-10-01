"""
CP1404/CP5632 - Practical 3
Files
This program ask the user for their name and then it writes it into a file.
"""

name = input("Name: ").capitalize()
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
    out_file.close()

with open("name.txt", "r") as in_file:
    name = in_file.readline()
    print(f"Your name is {name}")
    in_file.close()
