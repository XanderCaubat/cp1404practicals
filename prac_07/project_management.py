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
            is_valid = True
        except IndexError:
            print("Invalid input. Please enter the right date format.")
        except ValueError:
            print("Invalid date. Please enter the right date format.")


def add_project(projects):
    print("Let's add a new project")
    project_name = get_project_name()
    start_date = get_valid_date()
    priority_number = get_valid_number()
    cost_estimate = get_valid_cost()
    percent_complete = get_valid_percentage()
    project = Project(project_name, start_date, priority_number, cost_estimate, percent_complete)
    projects.append(project)


def get_valid_percentage():
    is_valid = False
    while not is_valid:
        try:
            percent_complete = float(input("Percent complete: "))
            while percent_complete < 1 or percent_complete > 100:
                print("Invalid percentage.")
                percent_complete = float(input("Percent complete: "))
                is_valid = True
        except ValueError:
            print("Invalid input.")
    return percent_complete


def get_valid_cost():
    is_valid = False
    while not is_valid:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            is_valid = True
        except ValueError:
            print("Invalid input.")
    return cost_estimate


def get_valid_number():
    is_valid = False
    while not is_valid:
        try:
            priority_number = int(input("Priority: "))
            is_valid = True
        except ValueError:
            print("Invalid integer.")
    return priority_number


def get_valid_date():
    is_valid = False
    while not is_valid:
        try:
            start_date = input("Start date (dd/mm/yyyy): ")
            parts = start_date.split('/')
            start_date = datetime.date(int(parts[2]), int(parts[1]), int(parts[0]))
            is_valid = True
        except IndexError:
            print("Invalid input. Please enter the right date format.")
        except ValueError:
            print("Invalid date. Please enter the right date format.")
    return start_date


def get_project_name():
    project_name = input("Name: ")
    while project_name == "":
        print("Project name cannot be blank.")
        project_name = input("Name: ")
    return project_name


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
