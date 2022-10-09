"""
CP1404/CP5632 - Practical 4
List Exercise
This program ask the users numbers and display information about them.
"""
MAX = 5


def main():
    numbers = []
    print("Enter 5 numbers.")
    get_numbers(numbers)
    display_information(numbers)


def display_information(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


def get_numbers(numbers):
    for i in range(MAX):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


main()


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted.")
else:
    print("Access denied")
