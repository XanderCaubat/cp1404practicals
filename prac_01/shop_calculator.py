"""
Xander Dino Caubat
CP1404/CP5632 Practical - Shop Calculator
This program calculates the total price of the items
"""
# pseudocode
# total amount = 0
# get number of items
# while number of items <= 0
#     print invalid number
# for i in number of items
#     get price of item
#     calculate total amount
# if total > 100
#     discounted amount = total amount - (total_amount * discount rate)
#     print discounted amount
# else
#     print total amount

# total_amount = 0
# number_of_items = int(input("Number of items: "))
# while number_of_items <= 0:
#     print("Invalid number of items!")
#     number_of_items = int(input("Number of items: "))
# for i in range(0, number_of_items):
#     price_of_item = float(input("Price of item: "))
#     total_amount += price_of_item
# if total_amount > 100:
#     discounted_amount = total_amount - (total_amount * .10)
#     print(f"10% discount applied for price over $100. Your total amount is ${discounted_amount:.2f}")
# else:
#     print(f"Your total amount is ${total_amount:.2f}")

min_length = 10
password = input("Password: ")
while len(password) < min_length:
    print("Invalid number of characters.")
    password = input("Password: ")
print("*" * len(password))
