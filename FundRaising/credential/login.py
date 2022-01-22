import csv
from Color_Console import *

color(text="purple", bg='light yellow')

def LogIN():
    found = 0
    user = {"id": None, "username": None}
    try:
        with open(r"C:\Users\ZiKa\Desktop\Python\lab03\credential\accounts.csv", "r", encoding="UTF-8") as accounts:
            ctext("Log in", text="green")
            while True:
                if found == 1:
                    break
                
                userName = input("Enter your user name: ")
                if(userName == "exit"): break
                password = input("Enter password: ")
                for x in accounts:
                    line = x.split(',')
                    u = line[1]
                    p = line[6].replace('\n', '')
                    if userName.strip() == u and password.strip() == p:
                        found = 1
                        user['id'] = x.split(',')[0]
                        user['username'] = u
                        ctext("Successfully Logged in", text="green")
                        break
                else:
                    accounts.seek(0)
                    ctext("Invalid user name or password.", text="red")
    except Exception as e:
        print(e)
    return user