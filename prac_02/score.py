"""
Practical 2
Xander Dino Caubat
Scores
Writing a new function that ask their user for their
score and print the result
"""


def main():
    score = get_score()
    determine_score(score)


def get_score():
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_score(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


main()
