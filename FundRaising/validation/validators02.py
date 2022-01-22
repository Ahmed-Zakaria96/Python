import re

def checkUserName(username, data):
    if len(data) == 0: return True
    usernames = [x['username'] for x in data]
    if username not in usernames:
        return checkName(username)
    else:
        print("User name already taken")
        return False


def checkName(name):
    return len(name) > 2 and len(name) < 20 and name.isalpha()


def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False

def checkPassword(password):

    SpecialSym =['$', '@', '#', '%']
    val = True

    if len(password) < 6:
        print('length should be at least 6')
        val = False
          
    if len(password) > 20:
        print('length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False

    return val if val else False

def checkConfirmPass(password, passwordConfirm):
    return password == passwordConfirm

def checkMobile(mobile):
    val = True
    Pattern = re.compile("^01(0|1|2|5){1}[0-9]{8}")
    if Pattern.match(mobile):
        print("Valid Mobile")
        return val
    else:
        val = False
        print("Invalid Mobile")
        return val

import datetime
def checkDate(date):
    isValidDate = True
    try:
        day, month, year = date.split('/')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print("Invalid Date")
        isValidDate = False

    return isValidDate