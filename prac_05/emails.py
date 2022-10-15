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
        email = confirm_name(email, email_to_names, name)
    print_dictionary(email_to_names)


def confirm_name(email, email_to_names, name):
    confirmation = input(f"Is you name {name}? (Y/N) ").lower()
    if confirmation != "y" and confirmation != "":
        name = input("Name: ").title()
    email_to_names[email] = name
    email = input("Email: ")
    return email


def print_dictionary(email_to_names):
    for email, name in email_to_names.items():
        print(f"{name:<15} ({email:})")


def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
