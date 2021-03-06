import os
from Color_Console import *
from classes import office
import menus
import helpers
import json

os.system("CLS")
color(text = "black", bg = "white")


ctext("\n\n\n\n\n\n\t\t\t\tWELCOME to STORY\n\n\n\n\n", text="blue")
os.system("pause")
# list to hold all offices
oL = []
while True:
    # show menu
    select = menus.mainMenu()
    if select == 6: break
    # add new office
    if select == 1:
        o = helpers.addNewOffice()
        oL.append(o)
    # show all offices
    elif select == 2:
        for i in oL:
            print(i)
    # show office data
    elif select == 3:
        offi = None
        while True:
            if offi: break
            oName = input("Enter office name: ")
            # check if office exist
            for i in oL:
                if i.name == oName:
                    offi = i
                    break
            else:
                ctext("Office not found.", text="red")
        # if successfull
        while True:
            # show office menu
            s = menus.officeMenu(offi)
            if s == 9: break
            # office methods
            helpers.switchSelection(offi, s)
            os.system("pause")
    # display total emp count
    elif select == 4:
        print(office.Office.employeeNum)
    # save data to json file
    elif select == 5:
        data = [off.prepareData() for off in oL]
        osD = {'offices': data}
        jsonObj = json.dumps(osD, indent=4)
        with open(r"C:\Users\ZiKa\Desktop\Python\lab04\story\emails\od.json", 'w') as OD:
            OD.write(jsonObj)
            
    os.system("pause")
