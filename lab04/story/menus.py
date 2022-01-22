from Color_Console import *
import os

def mainMenu():
    os.system("CLS")
    ctext("\n\nPlease Select required action from the following menu: \n", text="magenta")
    ctext("1- Add new office\n", text="cyan")
    ctext("2- View all offices\n", text="cyan")
    ctext("3- View office menu\n", text="cyan")
    ctext("4- Display current employees count\n", text="cyan")
    ctext("5- Export data to json file\n", text="cyan")
    ctext("6- Exit\n", text="cyan")

    while True:
        select = input("Enter your selection: ")
        if select.isdigit():
            select = int(select)
            if 1 <= select <= 6:
                return select

def officeMenu(offi):
    os.system("CLS")
    ctext(f"Showing {offi.name} Office data", text="blue")
    ctext("\nPlease Select required action from the following menu: \n", text="magenta")
    ctext("1- View all office employees\n", text="cyan")
    ctext("2- Search office for an emplyee\n", text="cyan")
    ctext("3- Hire new employee\n", text="cyan")
    ctext("4- Fire an employee\n", text="cyan")
    ctext("5- Check lateness\n", text="cyan")
    ctext("6- Reward an employee\n", text="cyan")
    ctext("7- Deduct and employee\n", text="cyan")
    ctext("8- Employee Menu\n", text="cyan")
    ctext("9- Back to main menu\n", text="cyan")

    while True:
        select = input("Enter your selection: ")
        if select.isdigit():
            select = int(select)
            if 1 <= select <= 9:
                return select

def employeeMenu(e):
    os.system("CLS")
    ctext(f"Showing employee {e.name} menu", text="blue")
    ctext(e, text="green")
    ctext("\nPlease Select required action from the following menu: \n", text="magenta")
    ctext("1- Set email", text="cyan")
    ctext("2- Set car", text="cyan")
    ctext("3- Set money\n", text="cyan")

    ctext("4- Send email", text="cyan")
    ctext("5- Buy items", text="cyan")
    ctext("6- Drive", text="cyan")
    ctext("7- ReFuel", text="cyan")
    ctext("8- Sleep", text="cyan")
    ctext("9- Eat", text="cyan")
    ctext("10- Main Menu", text="cyan")

    while True:
        select = input("Enter your selection: ")
        if select.isdigit():
            select = int(select)
            if 1 <= select <= 10:
                return select
