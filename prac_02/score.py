"""
Practical 2
Xander Dino Caubat
Scores
Writing a new function that ask their user for their
score and print the result
"""
import random


def main():
    score = get_score()
    grade = determine_score(score)
    print(grade)
    random_grade = determine_score(random.randint(0, 100))
    print(random_grade)


def get_score():
    """Ask the user to put in password"""
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_score(score):
    """Determine which grade the score belongs to"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
