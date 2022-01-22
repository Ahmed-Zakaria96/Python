import json
from validation import validators02 as v
import datetime
import os

def addProject(owner):
    os.system("CLS")
    print("Add new project: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", 'r') as projects:
            data = json.load(projects)
            projs = data['projects']
            L = len(projs)
            if L > 0:
                id = int(projs[L-1]['projectID']) + 1
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
                        print("End date should be greater than start date")
            proj = {
                'ownerID': OwnerID,
                'ownerName': OwnerName,
                'projectID': projectID,
                'projName': projName,
                'projDetails': projDetails,
                'projTarget' : projTarget,
                'projStart': projStart,
                'projEnd': projEnd
            }
            data['projects'].append(proj) 
            jsonObj = json.dumps(data, indent=4)
            try:
                with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", 'w') as projects:
                    projects.write(jsonObj)
                    print( "Successfully added new project.")
            except Exception as e:
                print(e)      
    except Exception as e:
        print(e)

def editProject(user):
    os.system("CLS")
    print("Edit project: ")

    projID = input("Enter project ID: ")
    if projID.isdigit(): projID = int(projID)
    s = editSubMenu()
    newValue = input("Enter new value: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", "r") as projects:
            data = json.load(projects)
            for i in data['projects']:
                if i['ownerID'] == user['id'] and i['projectID'] == projID:
                    k = list(i.keys())[s+2]
                    print(k)
                    i[k] = newValue
            jsonObj = json.dumps(data, indent=4)
            try:
                with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", 'w') as projects:
                    projects.write(jsonObj)
                    print("Successfully edited")
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


def deleteProject(user):
    os.system("CLS")
    print("Delete project: ")
    projID = input("Enter project ID: ")
    if projID.isdigit(): projID = int(projID)
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", "r", encoding="UTF-8") as projects:
            data = json.load(projects)
            for i in data['projects']:
                if i['ownerID'] == user['id'] and i['projectID'] == projID:
                    data['projects'].remove(i)
                    print("Successfully deleted project.")
                    break
            else:
                print("Not found")
            jsonObj = json.dumps(data, indent=4)
            try:
                with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", 'w') as projects:
                    projects.write(jsonObj)
            except Exception as e:
                print(e)     
    except Exception as e:
        print(e)

def viewAllProjects(user=None):
    os.system("CLS")
    print("All projects: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", "r", encoding="UTF-8") as projects:
            data = json.load(projects)
            count = 1
            for i in data['projects']:
                if user == None:
                    print(f"Project {count}: ")
                    printProj(i)
                    count += 1
                    print()
                else:
                    if i['ownerID'] == user['id']:
                        print(f"Project {count}: ")
                        printProj(i)
                        count += 1
                        print()

    except Exception as e:
        print(e)

def searchProject():
    os.system("CLS")
    print("Search for a project by title or description: ")
    title = input("Enter title to search for: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", "r", encoding="UTF-8") as projects:
            data = json.load(projects)
            found = 0
            for i in data['projects']:
                if title in i['projName'] or title in i['projDetails']:
                    found = 1
                    printProj(i)
            if not found: print("Not Found")
    except Exception as e:
        print(e)


def searchProjectDate():
    os.system("CLS")
    print("Search for a project by date: ")
    date = input("Enter Start Date to search from: ")
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\projects\projects.json", "r", encoding="UTF-8") as projects:
            data = json.load(projects)
            found = 0
            for i in data:
                if compareDates(i['projStart'], date):
                    found = 1
                    printProj(i)
            if not found: print("Not Found")
    except Exception as e:
        print(e)

def editSubMenu():
    print("Select field to edit: ")
    print("1- Title")
    print("2- Description")
    print("3- Target")
    print("4- Start Date")
    print("5- End Date")

    selection = input("Enter you select: ")
    if selection.isdigit():
        return int(selection)

def printProj(proj):
    for key, value in proj.items():
        print(key, ': ', value)

def compareDates(d1, d2):
    d1Day, d1Month, d1Year = d1.split('/')
    d1 = datetime.datetime(int(d1Year), int(d1Month), int(d1Day))
    d2Day, d2Month, d2Year = d2.split('/')
    d2 = datetime.datetime(int(d2Year), int(d2Month), int(d2Day))
    return d1 >= d2