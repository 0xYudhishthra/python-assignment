#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

#!/usr/bin/env python3


import os
import time
from types import DynamicClassAttribute

def main() :
    clearConsole()
    print("Welcome to Spiderman Online Food Service!")
    time.sleep(1)
    mainMenu()

def mainMenu():
    print("Please select any option below.", "1. Admin", "2. Customer", "3. Quit Program", sep=' \n')
    redirectUser(userInput())

def redirectUser(_): #Redirects user based on selected choice
    if _ == "1" :
        admin()

    elif _ == "2" :
        customerMenu()
    
    elif (_== "3") :
        quit()

    else :
        invalidInput()
        mainMenu()

def admin():
    print("\nAdmin Authentication Section")
    print("-" * 28)
    uName = input("Username: ")
    print("Checking if username exists...")
    time.sleep(1)
    authenticateAdmin(uName)

def readAdminFile(): #Reads admin file and converts it to list
    with open ('admins.txt', mode='r') as admin_file:
        admin_list = []
        for _ in range(1):
                next(admin_file)
        for row in admin_file:
            adminDetails=row.strip("\n").split(",")
            admin_list.append(adminDetails)
        return admin_list

def authenticateAdmin(uName): #Authenticates admin login details
     for data in readAdminFile():
      for i in range(0,len(data)):
        if uName == data[i]:
            print("Username found, please enter password\n")
            if input("Password: ") == data[i+1]:
                print("Authenticating...")
                time.sleep(1)
                adminMenu(uName)
            else: print("Invalid pass")
     if uName != data[i]:
        print("Username not found")
        time.sleep(0.5)
        print("Redirecting...\n")
        time.sleep(1)
        clearConsole()
        mainMenu()




def adminMenu(uName) :
    clearConsole()
    print("Welcome {}, what would you like to do today?\n".format(uName))
    print("1. Add food item","2. Modify food item","3. Display records","4. Search record","0. Back to Main Menu", sep='\n')
    redirectAdmin(userInput())

def redirectAdmin(_) : #Redirects admin based on selected choice
    if _ == "1" :
        foodCategory()
    elif _ == "2" :
        foodItem()
    elif _ == "3" :
        order()
    elif _ == "4" :
        checkPayment()
    elif _ == "0" :
        mainMenu()
    else :
        invalidInput()

def foodCategory() :
    clearConsole()
    print("\nPlease select any option below.")
    print("1. Add Food Category","2. Remove Food Category","3. Edit Food Category","4. Back to Main Menu","0. Back",sep='\n')
    redirectFoodCategory(userInput())

def redirectFoodCategory(_):
    if _ == "1" :
        addCategory()
    elif _ == "2" :
        removeCategory()
    elif _ == "3" :
        editCategory()
    elif _ == "4" :
        mainMenu()
    elif _ == "0" :
        adminMenu()
    else :
        invalidInput()
        foodCategory()

def addCategory() : pass
def removeCategory() : pass
def editCategory() :pass

def foodItem() :
    clearConsole()
    print("\nPlease select any option below.")
    print("1. Add Food Item","2. Remove Food Item","3. Edit Food Item","4. Back to Main Menu","0. Back",sep='\n')
    redirectFoodItem(userInput())
    
def redirectFoodItem(_):
    if _ == "1" :
        addFoodItem()
    elif _ == "2" :
        removeFoodItem()
    elif _ == "3" :
        editFoodItem()
    elif _ == "4" :
        mainMenu()
    elif _ == "0" :
        adminMenu()
    else :
        invalidInput()
        foodItem()

def addFoodItem() : pass
def removeFoodItem() : pass
def editFoodItem() : pass

def order() :
    clearConsole()
    print("\nPlease select any option below.")
    print("1. Cancel an order","2. Back to Main Menu","0. Back",sep='\n')
    redirectOrder(userInput())

def redirectOrder(_):
    if _ == "1" : 
        cancelOrder() 
    elif _ == "2" :
        mainMenu()
    elif _ == "0" :
        adminMenu()
    else : 
        invalidInput()
        order()

def cancelOrder() : pass
def checkPayment() : pass
def adminLogin() : pass

def customerMenu() :
    clearConsole()
    print("Please select any option below.")
    print("1. View Menu","2. Customer Login", "3. New Customer Registration", "4. Back to Main Menu", sep='\n')
    redirectCustomer(userInput())

def redirectCustomer(_):
    if _ == "1":
        viewCategoryList()
    elif _ == "2":
        authenticateCustomer()
    elif _ == "3":
        customerRegistration()
    elif _ == "4":
        mainMenu()
    else:
        invalidInput()
        customerMenu()

def regCustomerMenu():
    clearConsole()
    print("Welcome {}!, what would you like to do today?")
    print("1. View Item List", "2. View Item Details", "3. Add Food to Cart", "4. Checkout", "5. Main Menu", sep='\n')
    redirectRegCustomer(userInput())

def redirectRegCustomer(_):
    if _ == "1":
        viewItemList()
    elif _ =="2":
        viewItemDetail()
    elif _ == "3":
        addFoodToCart()
    elif _ =="4":
        checkout()
    elif _ == "5":
        mainMenu()
    else:
        invalidInput()
        regCustomerMenu()

def viewCategoryList() : pass
def viewItemList() : pass
def registered() : pass
def viewItemDetail() : pass
def viewCategoryDetail() : pass
def addFoodToCart() : pass
def checkout() : pass
def customerRegistration() : pass
def authenticateCustomer() : pass
def logout() : pass
def createFile() : pass
def deleteFile() : pass
def readFile() : pass
def writeFile() : pass

def clearConsole(): #Function to clear existing text in console
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def invalidInput() : #Function to flag user if improper input is submitted
    clearConsole()
    print("Invalid input. Please enter a number")
    time.sleep(1)
    clearConsole()

def quit() : #Exits program cleanly
    clearConsole()
    print("Exiting...")
    time.sleep(2)
    clearConsole()
    exit()

def userInput(): #Function to accept input from user
    return input("\nInput >> ")

main()

'''
lines=["colombian","na","na","na","na","na"]
with open('foods.txt', mode='a') as foods_file:
    for line in lines:
        foods_file.writelines(lines)

'''