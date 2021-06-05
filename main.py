#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

#!/usr/bin/env python3

import os
import time

def main() :
    clearConsole()
    print("Welcome to SOFS!")
    time.sleep(1)
    mainMenu(False, False)

def mainMenu(cSession , aSession) :
    print("Please select any option below.")
    print("1. Customer")
    print("2. Admin")
    if cSession | aSession :
        print("3. Logout")
    print("Q. Quit Program")

    uInput = userInput()

    if uInput == "1" :
        customer(cSession, aSession)

    elif uInput == "2" :
        admin(cSession, aSession)
    
    elif (uInput == "q") | (uInput == "Q") :
        quit()

    elif cSession | aSession :
        if uInput == "3" :
            logout(cSession, aSession)
    
    else :
        invalidInput()
        mainMenu(cSession, aSession)
        

def admin(cSession, aSession) :
    clearConsole()
    if aSession :
        adminMenu(cSession, aSession)
    else : 
        clearConsole()
        print("Please login as an Admin.")
        print("Do you want to go to login page? (Answer: y/n)")

        uInput = userInput()        

        if uInput == "y" :
            clearConsole()
            login(cSession, aSession)
        elif uInput == "n" :
            clearConsole()
            mainMenu(cSession, aSession)
        else :
            invalidInput()
            mainMenu(cSession, aSession)

def adminMenu(cSession , aSession) :
    clearConsole()
    print("Please select any option below.")
    print("1. Food Category")
    print("2. Food Items")
    print("3. View Orders")
    print("4. Payments")
    print("0. Back to Main Menu")

    uInput = userInput()

    if uInput == "1" :
        foodCategory(cSession, aSession)
    elif uInput == "2" :
        foodItem(cSession, aSession)
    elif uInput == "3" :
        orders(cSession, aSession)
    elif uInput == "4" :
        payment(cSession, aSession)
    elif uInput == "0" :
        mainMenu(cSession, aSession)
    else :
        invalidInput(cSession, aSession)

def foodCategory(cSession , aSession) :
    clearConsole()
    listOut("category")
    print("\nPlease select any option below.")
    print("1. Add Food Category")
    print("2. Remove Food Category")
    print("3. Edit Food Category")
    print("4. Back to Main Menu")
    print("0. Back")

    uInput = userInput()

    if uInput == "1" :
        addCategory(cSession, aSession)
    elif uInput == "2" :
        removeCategory(cSession, aSession)
    elif uInput == "3" :
        editCategory(cSession, aSession)
    elif uInput == "4" :
        mainMenu(cSession, aSession)
    elif uInput == "0" :
        adminMenu(cSession, aSession)
    else :
        invalidInput()
        foodCategory(cSession, aSession)

# def addCategory(cSession, aSession) :
# def removeCategory(cSession, aSession) :
# def editCategory(cSession, aSession) :

def foodItem(cSession, aSession) :
    clearConsole()
    listOut("item")
    print("\nPlease select any option below.")
    print("1. Add Food Item")
    print("2. Remove Food Item")
    print("3. Edit Food Item")
    print("4. Back to Main Menu")
    print("0. Back")

    uInput = userInput()

    if uInput == "1" :
        addFoodItem(cSession, aSession)
    elif uInput == "2" :
        removeFoodItem(cSession, aSession)
    elif uInput == "3" :
        editFoodItem(cSession, aSession)
    elif uInput == "4" :
        mainMenu(cSession, aSession)
    elif uInput == "0" :
        adminMenu(cSession, aSession)
    else :
        invalidInput()
        foodItem(cSession, aSession)

# def addFoodItem(cSession, aSession) :
# def removeFoodItem(cSession, aSession) :
# def editFoodItem(cSession, aSession) :

def order(cSession, aSession) :
    clearConsole()
    listOut("order")
    print("\nPlease select any option below.")
    print("1. Cancel an order")
    print("2. Back to Main Menu")
    print("0. Back")

    uInput = userInput()

    if uInput == "1" : 
        cancelOrder(cSession, aSession) 
    elif uInput == "2" :
        mainMenu(cSession, aSession)
    elif uInput == "0" :
        adminMenu(cSession, aSession)
    else : 
        invalidInput()
        order(cSession, aSession)

# def cancelOrder(cSession, aSession) :
# def checkPayment(cSession, aSession) :
# def adminLogin(cSession, aSession) :

def customer(cSession, aSession) :
    clearConsole()
    print("Please select any option below.")
    print("1. View Menu")
    
    cExist = cartExist()

    if cSession | aSession :
        if cExist :
            print("2. View Cart")
            print("3. Checkout")
            print("0. Back to Main Menu")
        else :
            print("0. Back to Main Menu")
            print("\nYour cart is empty!")
    else :
        print("2. Login")
        print("0. Back to Main Menu")

    uInput = userInput()

    if (cSession | aSession) & cExist :
        if uInput == "1" :
            viewCategoryList(cSession, aSession)
        elif uInput == "2" :
            viewCart(cSession, aSession)
        elif uInput == "3" :
            checkout(cSession, aSession)
        elif uInput == "4" :
            mainMenu(cSession, aSession)
        else :
            invalidInput()
            customer(cSession, aSession)
    elif cSession | aSession :
        if uInput == "1" :
            viewCategoryList(cSession, aSession)
        elif uInput == "0" :
            mainMenu(cSession, aSession)
        else :
            invalidInput()
            customer(cSession, aSession)
    else :
        if uInput == "1" :
            viewCart(cSession, aSession)
        elif uInput == "2" :
            login(cSession, aSession)
        elif uInput == "0" :
            mainMenu(cSession, aSession)
        else :
            invalidInput()
            customer(cSession, aSession)

# def viewCategoryList(cSession, aSession) :
# def viewItemList(cSession, aSession) :
# def registered(cSession, aSession) :
# def viewItemDetail(cSession, aSession) :
# def viewCategoryDetail(cSession, aSession) :
# def addFoodToCart(cSession, aSession) :
# def checkout(cSession, aSession) :

def quit() :
    clearConsole()
    print("Exiting...")
    time.sleep(2)
    clearConsole()
    exit()

# def register(cSession, aSession) :
# def login(cSession, aSession) :
# def logout(cSession, aSession) :
# def createFile() :
# def deleteFile() :
# def readFile() :
# def writeFile() :

def userInput() :
    return input("\nInput >> ")

def invalidInput() :
    clearConsole()
    print("Invalid input.")
    time.sleep(1)
    clearConsole()
    

def clearConsole() :
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

main()