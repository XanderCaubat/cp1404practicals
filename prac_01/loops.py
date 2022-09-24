"""
Xander Dino Caubat
CP1404/CP5632 Practical - Loops
A list of for loop exercise
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0-100
for i in range(0, 110, 10):
    print(i, end=' ')

# b. count down from 20-1
for i in range(20, 0, -1):
    print(i, end=' ')

# c. print n stars
stars = int(input("How many stars?: "))
for i in range(0, stars):
    print("*", end='')

# d. print n lines
stars = int(input("How many stars?: "))
for i in range(0, stars + 1):
    print('*' * i)
