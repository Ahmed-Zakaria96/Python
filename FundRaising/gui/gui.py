from credential import login, register
from projects import projects
from Color_Console import *

import os

color(text = "black", bg = "Light Yellow")

def home():
    os.system("CLS")
    ctext("Welcome to CrowdFunding Console App\n" , text = "red" , bg = "black")
    ctext("1- LogIn\n" , text = "green")
    ctext("2- Register\n" , text = "blue")

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
    ctext(f"Logged in as {user['username']}", text='blue')
    ctext("1- Add new project", text="magenta")
    ctext("2- View my projects", text="magenta")
    ctext("3- Edit my project", text="magenta")
    ctext("4- Delete my project", text="magenta")
    ctext("5- View all projects", text="magenta")
    ctext("6- Search a project by title or descption", text="magenta")
    ctext("7- Search a project by date", text="magenta")
    ctext("8- Exit", text="magenta")

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