from classes import person
from classes import car

class Employee(person.Person):

    def __init__(self, id, name, salary, distanceToWork, money, car=None, email=None):
        super().__init__(name, money)
        self.id = id
        self.car = car
        self._email = email
        self._salary = salary
        self.distanceToWork = distanceToWork

    def __str__(self):
        return f"""ID: {self.id} | Name: {self.name} | Email: {self.email} | Salary: {self.salary} | Money: {self.money}\n
        Mood: {self.mood} | Health: {self.healthRate}\n
        DistanceToWork: {self.distanceToWork} | Car: {self.car if self.car else None}"""

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount >= 1000:
            self._salary = amount
        else:
            print("Salary must be at least 1000.\nSalary was set to 1000")
            self._salary = 1000

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, mail):
        self._email = mail

    @staticmethod
    def validSalary(number):
        if isinstance(number, int):
            if number >= 1000:
                return True
        return False

    @staticmethod
    def validEmail(email):
        import re
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            print("Valid Email")
            return True
        else:
            print("Invalid Email")
            return False

    # drive the car
    def drive(self, d, v):
        if car:
            self.distanceToWork = self.car.run(self.distanceToWork, d, v)
        else:
            print("You don't have a car bro.")

    # refuel
    def refuel(self, f):
        return self.car.reFuel(f)

    # send mail
    def sendEmail(self, to, subject, msg, receiverName):
        import json
        try:
            with open(r"C:\Users\ZiKa\Desktop\Python\lab04\story\emails\emails.json", 'r') as emails:
                data = json.load(emails)
                mail = {
                    "From": self.email,
                    "To": to,
                    "Subject": subject,
                    "ReceiverName": receiverName + ",",
                    "Msg": msg,
                }
                data['emails'].append(mail)
                jsonObj = json.dumps(data, indent=4)

                try:
                    with open(r"C:\Users\ZiKa\Desktop\Python\lab04\story\emails\emails.json", 'w') as emails:
                        emails.write(jsonObj)
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

    # prepare employee data to be save in json file
    def prepareEmpData(self):
        data = {
            "empID" : self.id,
            "empName" : self.name,
            "empMood" : self.mood,
            "empHealth" : self.healthRate,
            "empSalary" : self.salary,
            "empMoney" : self.money,
            "empEmail" : self.email,
            "empCar" : self.car.prepareCarData() if self.car else None,
            "empDTW" : self.distanceToWork,
        }
        return data
