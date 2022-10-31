from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year}")


gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson.get_age())
