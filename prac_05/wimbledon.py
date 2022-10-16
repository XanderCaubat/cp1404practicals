"""
CP1404/CP5632 - Practical 5
Wimbledon
This program read the wimbledon csv file, process the data and display processed information
Estimate: 200 minutes
Actual:   minutes
"""

FILENAME = '../prac_05/wimbledon.csv'


def main():
    get_logs()
    logs = get_logs()
    champion_to_win_count, countries = process_logs(logs)
    print_results(champion_to_win_count, countries)


def print_results(champion_to_win_count, countries):
    print(champion_to_win_count)
    print("Wimbledon champions:")
    for champion in champion_to_win_count:
        print(f"{champion} {champion_to_win_count[champion]}")
    print(f"This {len(countries)} countries have won Wimbledon:")
    print(",".join(country for country in sorted(countries)))


def process_logs(logs):
    champion_to_win_count = {}
    countries = set()
    champions = [winner for winner in logs]
    for champion in champions:
        parts = champion.split(',')
        name = parts[2]
        countries.add(parts[1])
        win_count = champion_to_win_count.get(name, 0)
        champion_to_win_count[name] = win_count + 1
    return champion_to_win_count, countries


def get_logs():
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        lines = [line.strip() for line in in_file.readlines()]
        logs = set(lines)
    return sorted(logs)


main()
