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
    print("Welcome to Score Program\n(S)core\n(R)esult\n(D)isplay Stars\n(Q)uit")
    choice = input("Choice: ").upper()
    while choice != 'Q':
        if choice == 'S':
            pass
        elif choice == 'R':
            pass
        elif choice == 'D':
            pass
        else:
            print("Invalid input.")
            choice = input("Choice: ").upper()
    print("Thank you for using the Score Program. Have a nice day :)")


main()
