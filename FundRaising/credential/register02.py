import json
from validation import validators02 as v

def register():
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\credential\accounts.json", 'r+') as accounts:
            data = json.load(accounts)
            users = data['users']
            if (len(data['users']) == 0):
                id = 1
                data['users'] = []
            else:
                L = len(data['users'])
                id = int(data['users'][L-1]['id']) + 1
            print("Register new account: ")
            while True:
                userName = input("Enter Desired user name: ")
                userName = userName.strip()
                if v.checkUserName(userName, users): break

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

            user = {
                'id': id,
                'username': userName,
                'firstname': firstName,
                'lastname': lastName,
                'email': email,
                'mobile': mobile,
                'password': password
            }
            
            data['users'].append(user)
            jsonObj = json.dumps(data, indent=4)
            try:
                with open(r"C:\Users\ZiKa\Desktop\Python\lab03\credential\accounts.json", 'w') as accounts:
                    accounts.write(jsonObj)
                    print("Successfully registered")
            except Exception as e:
                print(e)
            
    except Exception as e:
         print(e)