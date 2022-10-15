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
    name = extract_name(email)

    while email != "":
        email = input("Email: ")

    print(name)


def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
