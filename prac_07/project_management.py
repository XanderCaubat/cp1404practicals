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
            pass
        elif choice == "U":
            pass
        print(MENU)
        choice = input(">>> ").upper()


def display_project_completion(projects):
    print("Incomplete projects:")
    incomplete_project = [project for project in sorted(projects) if not project.__is_complete__()]
    for project in incomplete_project:
        print(project)
    complete_project = [project for project in projects if project.__is_complete__()]
    print("Complete projects:")
    for project in complete_project:
        print(project)


def read_projects_file(projects):
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
