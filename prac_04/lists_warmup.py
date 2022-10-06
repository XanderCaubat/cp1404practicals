"""
CP1404/CP5632 - Practical 3
Warm-Up
This program prints a list of number.
"""

# this will print the list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]
# 3
# 2
# 1
# 1, 4, 1, 5, 9
# 1, 5
# True
# False
# False
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# answer 1
numbers[0] = "ten"
print(numbers)
# answer 2
numbers[-1] = 1
print(numbers[-1])
# answer 3
print(numbers[2:])
# answer 4
if 9 in numbers:
    print("9 is an element of numbers.")
