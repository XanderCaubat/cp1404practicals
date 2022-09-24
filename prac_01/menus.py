"""
Xander Dino Caubat
CP1404/CP5632 Practical - Menus
This program is based on a simple menu-driven program
"""

# pseudocode
# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

name = input("Enter name: ")
print(f"(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(f"(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>>").upper()
print("Finished")
