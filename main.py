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

'''
AUTHORS:
YUDHISHTHRA A/L S SUGUMARAN - TP061762
CHOONG WEI JUN - TP
'''