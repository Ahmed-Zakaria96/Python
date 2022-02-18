from Color_Console import *

class Office:

    employeeNum = 0

    def __init__(self, name, employees=[]):
        self.name = name
        # print(employees ??????????????????
        self.employees = employees

    def __str__(self):
        # on print show office name and number of employees
        return f"Name: {self.name} | Employees Count: {len(self.employees)}"

    # seach office employees
    def getEmployee(self, id):
        # search in office employees
        for i in self.employees:
            if i.id == id:
                return i
        else:
            ctext("Employee not found", text="red")
            return False

    # print all emps
    def getEmployees(self):
        if len(self.employees) > 0:
            for i in self.employees:
                ctext(i, text="green")
        else:
            ctext("Office does not have any employees yet.", text="red")

    # ha
    def hire(self, e):
        self.employees.append(e)
        # update over all emp count
        Office.employeeNum += 1

    # sekt el salama ya emp :)
    def fire(self, id):
        emp = self.getEmployee(id)
        if emp:
            self.employees.remove(emp)
            ctext(f"Fired {emp} :(", text="magenta")
            # update over all emp count
            Office.employeeNum -= 1
            return True

        else:
            ctext("Employee Not found.", text="red")
            return False

    # take money from emp
    def deduct(self, id, amount):
        emp = self.getEmployee(id)
        if emp:
            newSal = emp.salary - amount
            emp.salary = newSal
            ctext(emp, text="magenta")
            return True
        else:
            ctext("Employee Not Found", text="red")
            return False

    # give emp money
    def reward(self, id, amount):
        emp = self.getEmployee(id)
        if emp:
            emp.salary += amount
            ctext(emp, text="green")
            return True
        else:
            ctext("Employee Not Found", text="red")
            return False

    # check if the emp arrived late after 9
    def checkLateness(self, e, moveHour):
        late = Office.calcLateness(9, moveHour, e.distanceToWork, 10)
        # if late
        if not late:
            # reward
            self.reward(e.id, 10)
            ctext("rewarded +10", text="green")
        else:
            # deduct
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

    # prepare office data to be saved as json
    def prepareData(self):
        data = {
            "Office Name" : self.name,
            "Office Employees": [e.prepareEmpData() for e in self.employees]
        }
        return data
