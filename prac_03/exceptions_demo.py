"""
CP1404/CP5632 - Practical 3
Exceptions Demo
This program takes user's number inputs and calculates into fraction.
"""

is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")  # this occurs when the numbers entered are not integer
    except ZeroDivisionError:
        print("Cannot divide by zero!")  # this occurs when the numerator is divided by zero
print("Finished.")
