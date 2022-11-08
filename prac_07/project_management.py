"""
CP1404/CP5632 - Practical 7
Project Management Program
This program manage project priority, completion status and estimated cost
Estimate: 100 minutes
Actual:      minutes
"""

from prac_07.project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "


def main():
    projects = []
    read_projects_file(projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_project_completion(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MENU)
        choice = input(">>> ").upper()


def add_project(projects):
    print("Let's add a new project")
    project_name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority_number = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = float(input("Percent complete: "))
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


def read_projects_file(projects):
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
