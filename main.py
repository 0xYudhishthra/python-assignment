#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

#!/usr/bin/env python3
from pyfiglet import Figlet # Importing module to decorate welcome message
import os, time

'''
This part of code is to display the name of the program
'''
from pyfiglet import Figlet
f = Figlet(font='univers')
print (f.renderText('S O F S'))

def main() :
    print("Types of dashboard:\n1. Customer\n2. Administrator\nQ. Quit")
    adminOrCustomer = input("Which dasboard would you like to get into?\n>> ")
    if adminOrCustomer == "1" :
        dashboardCustomer()
    elif adminOrCustomer == "2":
        dashboardAdmin()
    elif (adminOrCustomer == "q") | (adminOrCustomer == "Q"):
        exit()
    else: main()

def dashboardAdmin():
    print("admin")

def dashboardCustomer():
    print("customer")

def exit():
    print("\nExiting Program.")
    time.sleep(0.5)
    os._exit(0)

main()



