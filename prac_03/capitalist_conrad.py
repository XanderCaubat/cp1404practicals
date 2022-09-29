"""
CP1404/CP5632 - Practical 3
Capitalist Conrad
This program will simulate stock-price.
"""

import random
MAX_INCREASE = 0.175  # modified 10% to 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0    # change 0.01 to 1.0
MAX_PRICE = 100.0   # change 1000.0 to 100.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
number_of_days = 0
print("${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # modified string formatting of print statement
    print(f"On day {number_of_days} price is: ${price:,.2f}")
