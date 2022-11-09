"""
CP1404/CP5632 - Practical 7
Project Management Program
This program manage project priority, completion status and estimated cost
Estimate: 100 minutes
Actual:      minutes
"""
import datetime

from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "


def main():
    projects = []
    filename = "projects.txt"
    read_file(filename, projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = load_file(filename, projects)
        elif choice == "S":
            save_project(filename, projects)
        elif choice == "D":
            display_project_completion(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()


def save_project(filename, projects):
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}"
                  f"\t{project.percent}", file=out_file)
        projects.clear()


def load_file(filename, projects):
    if len(projects) != 0:
        print("You are still managing an existing file. Please save to load a new one")
    else:
        filename = input("Filename: ")
        read_file(filename, projects)
    return filename


def read_file(filename, projects):
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            parts[1] = parts[1].split('/')
            date = datetime.date(int(parts[1][2]), int(parts[1][1]), int(parts[1][0]))
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


def filter_project(projects):
    is_valid = False
    while not is_valid:
        try:
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            parts = filter_date.split('/')
            date = datetime.date(int(parts[2]), int(parts[1]), int(parts[0]))
            for project in projects:
                if project.start_date >= date:
                    print(project)
            return True
        except IndexError:
            print("Invalid input. Please enter the right date format.")
        except ValueError:
            print("Invalid date. Please enter the right date format. ")


def add_project(projects):
    print("Let's add a new project")
    project_name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority_number = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = float(input("Percent complete: "))
    parts = start_date.split('/')
    start_date = datetime.date(int(parts[2]), int(parts[1]), int(parts[0]))
    project = Project(project_name, start_date, priority_number, cost_estimate, percent_complete)
    projects.append(project)


def update_project(projects):
    for i, project in enumerate(projects, 0):
        print(i, project)
    project_choice = (int(input("Project choice: ")))
    print(projects[project_choice])
    new_percent = float(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    projects[project_choice].percent = new_percent
    projects[project_choice].priority = new_priority


def display_project_completion(projects):
    print("Incomplete projects:")
    incomplete_project = [project for project in sorted(projects) if not project.is_complete()]
    for project in incomplete_project:
        print(" ", project)
    complete_project = [project for project in sorted(projects) if project.is_complete()]
    print("Complete projects:")
    for project in complete_project:
        print(" ", project)


main()
