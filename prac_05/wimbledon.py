"""
CP1404/CP5632 - Practical 5
Wimbledon
This program read the wimbledon csv file, process the data and display processed information
Estimate: 200 minutes
Actual:   minutes
"""


def main():
    champion_to_win_count = {}
    with open('../prac_05/wimbledon.csv', 'r', encoding="utf-8-sig") as in_file:
        lines = [line.strip() for line in in_file.readlines()]
        winners = set(lines)
        champions = [winner for winner in winners]
        for champion in champions:
            parts = champion.split(',')
            name = parts[2]
            win_count = champion_to_win_count.get(name, 0)
            champion_to_win_count[name] = win_count + 1
    print("Wimbledon champions:")
    for champion in champion_to_win_count:
        print(f"{champion} {champion_to_win_count[champion]}")


main()
