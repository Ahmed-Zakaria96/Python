import csv
import json

def LogIN():
    found = 0
    user = {"id": None, "username": None}
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\credential\accounts.json") as accounts:
            data = json.load(accounts)
            users = data['users']
            print("Login")
            while True:
                if found == 1:
                    break
                userName = input("Enter your user name: ")
                password = input("Enter password: ")
                for x in users:
                    if userName == x['username'] and password == x['password']:
                        found = 1
                        user['id'] = x['id']
                        user['username'] = x['username']
                        print("Successfully Logged in")
                        break
                else:
                    print("Invalid user name or password.")
    except Exception as e:
        print(e)
    return user