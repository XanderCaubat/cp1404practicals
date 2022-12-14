"""
CP1404/CP5632 - Practical 5
State Names
This program display the full name of an acronym of the state.
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid Key Input!")
    state_code = input("Enter short state: ").upper()
if CODE_TO_NAME == {}:
    print("Dictionary does not exist!")
else:
    for state_code in CODE_TO_NAME:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
