"""
CP1404/CP5632 - Practical 5
Emails
This program stores user's emails and name in a dictionary.
Estimate: 100 minutes
Actual:    minutes
"""


def main():
    email_to_names = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is you name {name}? (Y/N) ").lower()
        if confirmation == "y" or confirmation == "":
            email_to_names[email] = name
        elif confirmation == "n":
            actual_name = input("Name: ")
            email_to_names[email] = actual_name
        email = input("Email: ")
    print_dictionary(email_to_names)


def print_dictionary(email_to_names):
    try:
        max_length = max(len(email_to_names[name]) for name in email_to_names)
        for email, name in email_to_names.items():
            print(f"{name:{max_length}} ({email})")
    except ValueError:
        print("Invalid input!")


def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
