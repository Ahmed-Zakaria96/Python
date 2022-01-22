from credential import login02 as login
from credential import register02 as register
from projects import projects02 as projects

import os

def home():
    print("Welcome to CrowdFunding Console App\n")
    print("1- LogIn")
    print("2- Register")
    selection = input("Enter your selection: ")
    if selection.isdigit():
        selection = int(selection)
    if selection == 1:
        os.system("CLS")
        user = login.LogIN()
        os.system("pause")
        if user:
            while True:
                userSelect = userMenu(user)
                if userSelect == 8: break
                MapSelect(userSelect, user)
                os.system("pause")
    elif selection == 2:
        os.system("CLS")
        register.register()
        os.system("pause")
        os.system("CLS")
        user = login.LogIN()
        if user:
            while True:
                userSelect = userMenu(user)
                if userSelect == 8: break
                MapSelect(userSelect, user)
                os.system("pause")

def userMenu(user):
    os.system("CLS")
    print(f"Logged in as {user['username']}")
    print("1- Add new project")
    print("2- View my projects")
    print("3- Edit my project")
    print("4- Delete my project")
    print("5- View all projects")
    print("6- Search a project by title or descption")
    print("7- Search a project by date")
    print("8- Exit")

    selection = input("Enter your selection: ")
    if selection.isdigit():
        return int(selection)

def MapSelect(selection, user):
    if selection == 1:
        projects.addProject(user)
    elif selection == 2:
        projects.viewAllProjects(user)
    elif selection == 3:
        projects.editProject(user)
    elif selection == 4:
        projects.deleteProject(user)
    elif selection == 5:
        projects.viewAllProjects()
    elif selection == 6:
        projects.searchProject()
    elif selection == 7:
        projects.searchProjectDate()
    elif selection == 8:
        print("Exiting....")