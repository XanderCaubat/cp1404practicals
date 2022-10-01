"""
CP1404/CP5632 - Practical 3
Exceptions Demo
This program takes user's number inputs and calculates into fraction.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:  # this if statement catches the input if its 0 to avoid the possibility of ZeroDivisionError
        print("0")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")  # this occurs when input is not an integer
except ZeroDivisionError:
    print("Cannot divide by zero!")  # this occurs when the numerator is divided by zero
