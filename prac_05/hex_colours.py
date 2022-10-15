"""
CP1404/CP5632 - Practical 5
Hex Colours
This program ask the user to look up a hexadecimal colour.
"""

# the dictionary is not constant as the content could change hence it is not in all caps
colour_to_hexes = {"aliceblue": "f0f8ff", "baby pink": "#f4c2c2", "cadetblue": "#5f9ea0", "daffodil": "#ffff31",
                   "ebony": "555d50", "fawn": "#e5aa70", "gainsboro": "#dcdcdc", "gray": "#bebebe",
                   "iceberg": "#71a6d2",
                   "jade": "00a86b"}
colour = input("Choose colour? ").lower()
while colour != "":
    if colour in colour_to_hexes:
        print(f"The hex number of {colour} is {colour_to_hexes[colour]}")
    else:
        print("Invalid key input!")
    colour = input("Colour? ").lower()
print("Thank you for using the Color to Hex program, have a nice day!")
