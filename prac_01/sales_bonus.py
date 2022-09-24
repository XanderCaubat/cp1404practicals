"""
Xander Dino Caubat
CP1404/CP5632 Practical - Sales Bonus
A program to calculate and display a user's bonus based on sales.
"""

# pseudocode
# get sales
# while sales >= 0
#     calculate bonus
#     get sales
# do next thing

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * .15
        print(f"Your bonus is ${bonus:.2f}")
    elif sales < 1000:
        bonus = sales * .10
        print(f"Your bonus is ${bonus:.2f}")
    else:
        "Invalid Input"
    sales = float(input("Enter sales: $"))

