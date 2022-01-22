import csv
from validation import validators as v
import datetime
import os
from Color_Console import *

def addProject(owner):
    os.system("CLS")
    ctext("Add new project: ", text="magenta")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "a+", encoding="UTF-8", newline='') as projects:
            csvwriter = csv.writer(projects, delimiter=',')
            projects.seek(0)
            data = projects.readlines()
            if len(data) > 0:
                id = int(data[-1].split(',')[2]) + 1
            else:
                id = 1
            OwnerID = owner['id']
            projectID = id
            OwnerName = owner['username']
            while True:
                projName = input("Enter project name: ")
                if v.checkName(projName): break 
            projDetails = input("Enter project details: ")
            projTarget = input("Enter target: ")
            while True:
                projStart = input("Enter start date in format 'dd/mm/yy: ")
                if v.checkDate(projStart) == True: break
            while True:
                projEnd = input("Enter end date in format 'dd/mm/yy: ")
                if v.checkDate(projEnd):
                    if compareDates(projEnd, projStart):
                        break
                    else:
                        ctext("End date should be greater than start date", text="red")

            csvwriter.writerow([OwnerID, OwnerName, projectID, projName, projDetails, projTarget, projStart, projEnd])
            ctext("Successfully added new project.", text="green")
    except Exception as e:
        print(e)

def editProject(user):
    os.system("CLS")
    ctext("Edit project: ", text = "magenta")

    lines = []
    projID = input("Enter project ID: ")
    if projID.isdigit(): projID = int(projID)
    s = editSubMenu()
    newValue = input("Enter new value: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "r", encoding="UTF-8", newline='') as projects:
            data = projects.readlines()
            for i in data:
                proj = i.replace('\n', '').split(',')
                proj = i.split(',')
                if proj[0] == user['id'] and int(proj[2]) == projID:
                    proj[s+2] = newValue
                lines.append(proj)
    except Exception as e:
        print(e)

    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "w", encoding="UTF-8", newline='') as projects:
            csvwriter = csv.writer(projects, delimiter=',', lineterminator='')
            csvwriter.writerows(lines)
            ctext("Successfullty edited project data", text="green")
    except Exception as e:
        print(e)


def deleteProject(user):
    os.system("CLS")
    ctext("Delete project: ", text="magenta")
    projID = input("Enter project ID: ")
    if projID.isdigit(): projID = int(projID)
    lines = []
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "r", encoding="UTF-8", newline='') as projects:
            data = projects.readlines()
            for i in data:
                proj = i.replace('\n', '')
                proj = [p.strip() for p in proj.split(',')]
                if proj[0] == user['id'] and int(proj[2]) == projID:
                    ctext("Successfully deleted project.", text="green")
                    continue
                lines.append(proj)
    except Exception as e:
        print(e)

    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "w", encoding="UTF-8", newline='') as projects:
            csvwriter = csv.writer(projects, delimiter=',', lineterminator='\n')
            csvwriter.writerows(lines)
    except Exception as e:
        print(e)

def viewAllProjects(user=None):
    os.system("CLS")
    ctext("All projects: ", text="magenta")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "r", encoding="UTF-8") as projects:
            data = projects.readlines()
            for i in data:
                proj = i.replace('\n', '').split(',')
                proj = i.split(',')
                if user == None:
                    printProj(proj)
                else:
                    if proj[0] == user['id']:
                        printProj(proj)
    except Exception as e:
        print(e)

def searchProject():
    os.system("CLS")
    ctext("Search for a project by title or description: ", text="magenta")
    title = input("Enter title to search for: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "r", encoding="UTF-8") as projects:
            data = projects.readlines()
            for i in data:
                proj = i.replace('\n', '').split(',')
                proj = i.split(',')
                if title in proj[3] or title in proj[4]:
                    printProj(proj)
    except Exception as e:
        print(e)

def searchProjectDate():
    os.system("CLS")
    ctext("Search for a project by date: ", text="magenta")
    date = input("Enter Start Date to search from: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.csv", "r", encoding="UTF-8") as projects:
            data = projects.readlines()
            for i in data:
                proj = i.replace('\n', '').split(',')
                proj = i.split(',')
                if compareDates(proj[6], date):
                    printProj(proj)
    except Exception as e:
        print(e)

def editSubMenu():
    ctext("Select field to edit", text="blue")
    ctext("1- Title", text="cyan")
    ctext("2- Description", text="cyan")
    ctext("3- Target", text="cyan")
    ctext("4- Start Date", text="cyan")
    ctext("5- End Date", text="cyan")

    selection = input("Enter you select")
    if selection.isdigit():
        return int(selection)

def printProj(proj):
    ctext(f"Owner: {proj[1]}", text="cyan")
    ctext(f"Project ID: {proj[2]}", text="cyan")
    ctext(f"Title: {proj[3]}", text="cyan")
    ctext(f"Description: {proj[4]}", text="cyan")
    ctext(f"Target: {proj[5]}", text="cyan")
    ctext(f"Start Date: {proj[6]}", text="cyan")
    ctext(f"End Date: {proj[7]}", text="cyan")

def compareDates(d1, d2):
    d1Day, d1Month, d1Year = d1.split('/')
    d1 = datetime.datetime(int(d1Year), int(d1Month), int(d1Day))
    d2Day, d2Month, d2Year = d2.split('/')
    d2 = datetime.datetime(int(d2Year), int(d2Month), int(d2Day))
    return d1 >= d2