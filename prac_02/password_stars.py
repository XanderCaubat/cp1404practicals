"""
Practical 02
Xander Dino Caubat
Password Check with Functions
Refactoring this program to use functions
"""


def main():
    min_length = 10
    password = get_password(min_length)
    print_asterisk(password)


def get_password(min_length):
    """Ask the user for a password"""
    password = input("Password: ")
    while len(password) < min_length:
        print("Invalid number of characters (min. 10).")
        password = input("Password: ")
    return password


def print_asterisk(password):
    print("*" * len(password))


main()
