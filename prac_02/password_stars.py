min_length = 10
password = input("Password: ")
while len(password) < min_length:
    print("Invalid number of characters (min. 10).")
    password = input("Password: ")
print("*" * len(password))
