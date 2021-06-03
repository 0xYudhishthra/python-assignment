<<<<<<< HEAD
#YUDHISHTHRA A/L S SUGUMARAN - TP061762
#Choong Wei Jun - TP061867

import os

def main() :
    print("Types of dashboard:\n1. Customer\n2. Administrator\nQ. Quit")
    adminOrCustomer = input("Which dasboard would you like to get into?\n>> ")
    if adminOrCustomer == "1" :
        dashboardCustomer()
    elif adminOrCustomer == "2":
        dashboardAdmin()
    elif (adminOrCustomer == "q") | (adminOrCustomer == "Q"):
        os._exit(0)
    else: main()

def dashboardAdmin():
    print("admin")

def dashboardCustomer():
    print("customer")

main()
=======
'''
AUTHORS:
YUDHISHTHRA A/L S SUGUMARAN - TP061762
CHOONG WEI JUN - TP
'''

>>>>>>> c917a7106aad50bfb0f12ad6b36af24c46390bdb
