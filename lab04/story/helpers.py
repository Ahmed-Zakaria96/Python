from classes import office
from classes import car
from classes import employee
import menus
import validators as v
from Color_Console import *
import os

def addNewOffice():
    while True:
        name = input("Enter office name: ")
        check = v.checkName(name)
        if check:
            break

    offi = office.Office(name, employees=[])
    return offi

def switchSelection(o, s):
    if s == 1:
        o.getEmployees()

    elif s == 2:
        while True:
            id = input("Enter Employee id: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                ctext("Please enter valid id.", text="red")
        emp = o.getEmployee(id)
        if emp:
            ctext(emp, text="green")
        else:
            ctext("Employee not found.", text="red")

    elif s == 3:
        e = addEmployee()
        o.hire(e)

    elif s == 4:
        while True:
            id = input("Enter Employee id: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                ctext("Please enter valid id.", text="red")
        e = o.getEmployee(id)
        if e:
            o.fire(id)

    elif s == 5:
        while True:
            id = input("Enter Employee id: ")
            if id.isdigit():
                id = int(id)
                e = o.getEmployee(id)
                if e:
                    break
            else:
                ctext("Please enter valid id.", text="red")
        while True:
            move = input("Enter move hour: ")
            if move.isdigit():
                move = int(move)
                break
            else:
                ctext("Please enter valid hour.", text="red")

        o.checkLateness(e, move)

    elif s == 6:
        while True:
            id = input("Enter Employee id: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                ctext("Please enter valid id.", text="red")
        while True:
            amount = input("Enter reward amount: ")
            if amount.isdigit():
                amount = int(amount)
                break
            else:
                ctext("Please enter valid reward amount.", text="red")
        check = o.reward(id, amount)
        if check:
            ctext("Successfully added the reward", text="green")
        else:
            ctext("Somthing wrong happened", text="red")

    elif s == 7:
        while True:
            id = input("Enter Employee id: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                ctext("Please enter valid id.", text="red")
        while True:
            amount = input("Enter deduct amount: ")
            if amount.isdigit():
                amount = int(amount)
                break
            else:
                ctext("Please enter valid reward amount.", text="red")
        check = o.deduct(id, amount)
        if check:
            ctext("Successfully added the deduct", text="magenta")
        else:
            ctext("Somthing wrong happened", text="red")

    elif s == 8:
        while True:
            id = input("Enter Employee id: ")
            if id.isdigit():
                id = int(id)
                break
            else:
                ctext("Please enter valid id.", text="red")
        while True:
            e = o.getEmployee(id)
            if e:
                m = menus.employeeMenu(e)
                if m == 10:
                    break
                employeeMethods(e, m)
            else:
                break
            os.system("pause")

    elif s == 9:
        return s

def addEmployee():
    while True:
        id = input("Enter employee id: ")
        if id.isdigit():
            id = int(id)
            break

    name = input("Enter employee name: ")
    while True:
        salary = input("Enter employee salary: ")
        if salary.isdigit():
            salary = int(salary)
            if salary >= 1000:
                break
            else:
                ctext("Salary must be at least 1000.", text="red")
    while True:
        distanceToWork = input("Enter distanceToWork: ")
        if distanceToWork.isdigit():
            distanceToWork = int(distanceToWork)
            break
    while True:
        money = input("Enter money: ")
        if money.isdigit():
            money = int(money)
            break

    e = employee.Employee(
        id=id,
        name=name,
        salary=salary,
        distanceToWork=distanceToWork,
        money=money,
    )
    return e

def employeeMethods(e, m):
    if m == 1:
        while True:
            mail = input("Enter your Email: ")
            check = employee.Employee.validEmail(mail)
            if check:
                e.email = mail
                break

    elif m == 2:
        cName = input("Enter you car name: ")
        fRate = input("Enter Fuel rate: ")
        if fRate.isdigit():
            c = car.Car(cName, int(fRate))
            e.car = c
            ctext("Car changed Successfully.", text="green")

    elif m == 3:
        money = input("Enter Money amout: ")
        if money.isdigit():
            e.money = int(money)
        else:
            ctext("Invalid amount.", text="red")
    elif m == 4:
        while True:
            eTo = input("Enter Receiver email: ")
            if employee.Employee.validEmail(eTo):
                break
        subj = input("Enter subject: ")
        recName = input("Enter receiver name: ")
        msg = input("Enter message: ")
        e.sendEmail(eTo, subj, msg, recName)
        ctext("MSG was sent Successfully.", text="green")

    elif m == 5:
        items = input("Enter amount of number of items: ")
        if items.isdigit():
            e.buy(int(items))
        else:
            ctext("Invalid number of items", text="red")

    elif m == 6:
        if e.car:
            while True:
                d = input("Enter distance: ")
                if d.isdigit():
                    d = int(d)
                    break
            while True:
                v = input("Enter velocity: ")
                if v.isdigit():
                    v = int(v)
                    break
            e.drive(d, v)
        else:
            ctext("You dont have a car set a car first.", text="red")

    elif m == 7:
        if e.car:
            while True:
                f = input("Enter fuel amount: ")
                if f.isdigit():
                    f = int(f)
                    break
            e.refuel(f)
        else:
            ctext("You dont have a car set a car first.", text="red")

    elif m == 8:
        while True:
            s = input("Enter sleep hours: ")
            if s.isdigit():
                s = int(s)
                break
        e.sleep(s)

    elif m == 9:
        while True:
            ms = input("Enter number of meals: ")
            if ms.isdigit():
                ms = int(ms)
                break
        e.eat(ms)

    elif m == 10:
        return m
