import csv
from validation import validators as v

def register():
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\credential\accounts.csv", "a+", encoding="UTF-8", newline='') as accounts:
            csvwriter = csv.writer(accounts, delimiter=',')
            accounts.seek(0)
            data = accounts.readlines()
            if (len(data) == 0):
                id = 1
            else:
                id = int(data[-1].split(',')[0]) + 1
            print("Register new account: ")
            while True:
                userName = input("Enter Desired user name: ")
                userName = userName.strip()
                if v.checkUserName(userName, data): break

            while True:
                firstName = input("Enter your first name: ")
                firstName = firstName.strip()
                if v.checkName(firstName): break

            while True:
                lastName = input("Enter your last name: ")
                lastName = lastName.strip()
                if v.checkName(lastName): break

            while True:
                email = input("Enter you email: ")
                email = email.strip()
                if v.checkEmail(email): break

            while True:
                mobile = input("Enter your mobile Number: ")
                mobile = mobile.strip()
                if v.checkMobile(mobile): break

            while True:
                password = input("Enter your password: ")
                if v.checkPassword(password): break

            while True:
                confirmPass = input("Confirm password: ")
                if v.checkConfirmPass(password, confirmPass): break


            csvwriter.writerow([id, userName, firstName, lastName, email, mobile, password])
            print("Successfully registered")
    except Exception as e:
        print(e)