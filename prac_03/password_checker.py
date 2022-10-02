"""
CP1404/CP5632 - Practical
Password checker
This program ask the user the password and checks it.
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        count_lower += int(char.islower())
        count_upper += int(char.isupper())
        count_digit += int(char.isdigit())
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    # this if statement only happens when the constant "special characters required"  is set to true
    # then passed in a list of the special characters to a variable to be checked for special count
    if SPECIAL_CHARS_REQUIRED:
        special_characters = SPECIAL_CHARACTERS
        for char in password:
            if char in special_characters:
                count_special += 1
        if count_special == 0:
            return False
    return True


main()
