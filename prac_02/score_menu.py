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
    score = 0
    print_menu()
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'S':
            score = get_score()
        elif choice == 'R':
            display_result(score)
        elif choice == 'D':
            print_stars(score)
        else:
            print("Invalid input.")
        print_menu()
        choice = input(">>>: ").upper()
    print("Thank you for using the Score Program. Have a nice day :)")


def print_menu():
    print("\nWelcome to Score Program")
    print("(S)core\n(R)esult\n(D)isplay Stars\n(Q)uit\n")


def display_result(score):
    grade = determine_score(score)
    length = len(grade)
    print("*" * length)
    print(grade)
    print("*" * length)


def get_score():
    """determine password is valid"""
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_score(score):
    """determine which grade the score belongs to"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def print_stars(score):
    """print stars according to the score"""
    if score <= 0:
        print("There is no score recorded.")
    elif score > 0:
        for i in range(round(score)):
            print("*", end='')


main()
