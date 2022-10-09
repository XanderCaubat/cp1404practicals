"""
CP1404/CP5632 - Practical 4
Total Income
This program calculate and display the users total income.
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


# removed the second parameter as incomes is all we needed for this function
def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:.2f} Total: ${total:.2f}")


main()
