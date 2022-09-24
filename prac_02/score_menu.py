"""
Practical 2
Xander Dino Caubat
Menu
Write a complete Python program following the standard structure that
uses a main and other functions
"""


# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>

def main():
    print("Welcome to Score Program\n(R)esult\n(D)isplay Stars\n(Q)uit")
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'R':
            display_result()
        elif choice == 'D':
            pass
        else:
            print("Invalid input.")
        choice = input("Choice: ").upper()
    print("Thank you for using the Score Program. Have a nice day :)")


def display_result():
    score = get_score()
    grade = determine_score(score)
    print(grade)


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
