from Color_Console import *

class Office:

    employeeNum = 0

    def __init__(self, name, employees=[]):
        self.name = name
        # print(employees ??????????????????
        self.employees = employees

    def __str__(self):
        return f"Name: {self.name} | Employees Count: {len(self.employees)}"
    def getEmployee(self, id):
        for i in self.employees:
            if i.id == id:
                return i
        else:
            ctext("Employee not found", text="red")
            return False

    def getEmployees(self):
        if len(self.employees) > 0:
            for i in self.employees:
                ctext(i, text="green")
        else:
            ctext("Office does not have any employees yet.", text="red")

    def hire(self, e):
        self.employees.append(e)
        Office.employeeNum += 1

    def fire(self, id):
        for i in self.employees:
            if i.id == id:
                self.employees.remove(i)
                ctext(f"Fired {i} :(", text="magenta")
                Office.employeeNum -= 1
                return True
        else:
            ctext("Employee Not found.", text="red")
            return False

    def deduct(self, id, amount):
        emp = self.getEmployee(id)
        if emp:
            newSal = emp.salary - amount
            emp.salary = newSal
            return True
        else:
            ctext("Employee Not Found", text="red")
            return False

    def reward(self, id, amount):
        emp = self.getEmployee(id)
        if emp:
            emp.salary += amount
            return True
        else:
            ctext("Employee Not Found", text="red")
            return False

    def checkLateness(self, e, moveHour):
        late = Office.calcLateness(9, moveHour, e.distanceToWork, 10)
        if not late:
            self.reward(e.id, 10)
            ctext("rewarded +10", text="green")
        else:
            self.deduct(e.id, 10)
            ctext("deducted -10", text="red")

    @staticmethod
    def calcLateness(targetHour, moveHour, d, v):
        t = d / v
        arrive = moveHour + t
        if arrive > targetHour:
            ctext(f"Employee arrived at {arrive}", text="yellow")
            return True
        else:
            return False

    def prepareData(self):
        data = {
            "Office Name" : self.name,
            "Office Employees": [e.prepareEmpData() for e in self.employees]
        }
        return data
