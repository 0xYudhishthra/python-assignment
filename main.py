#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

"""
Code Structure
1. Import necessary external modules
2. Declaring functions to read text files and convert it to lists
3. Declaring functions that can be used in any part of the program
4. Declaring functions for admin dashboard
    0. Login to Access System (Done)
    1. Add food item by category (In progress)
    2. Modify food item (Edit, Delete, Update)
    3. Display Records of Food Category (Done)
    4. Display Records of Food Items by Category (Done)
    5. Display Records of Customer Orders (Done)
    6. Display Records of Customer Payments (Done)
    7. Search Specific Customer Order Record (Done)
    8. Search Specific Customer Payment Record
    9. Exit
5. Declaring functions for guest dashboard   
    0. View all food items as per category
    1. New customer registration to access other details
    2. Exit
6. Declaring functions for Registered Customer Dashboard
    0. Login to access system
    1. View detail of food category
    2. View detail of food items
    3. Select food item and add to cart
    4. Do payment to confirm order
    5. Exit
7. Declaring main greeting page
8. Execute main
"""

'''IMPORTING NECESSARY EXTERNAL MODULES'''
#!/usr/bin/env python3
import os
import time
from typing import Type

'''DECLARING FUNCTIONS TO CONVERT TEXT FILES TO LISTS'''
def readAdminDetailsFile(): #Reads admin file and converts it to list
    with open ('adminDetails.txt', mode='r') as adminFile:
        admin_list = []
        skipFileLine(1,adminFile)
        for row in adminFile:
            adminDetails=row.strip("\n").replace(" | "," ").split(" ")
            admin_list.append(adminDetails)
        return admin_list

def readFoodDetailsFile(): #Function to convert foodDetails text file to list
    foodDetails=[]
    with open ('foodDetails.txt', mode='r') as foodDetailsFile:
        skipFileLine(6,foodDetailsFile) 
        for row in foodDetailsFile:
            if row.startswith("_"):
                skipFileLine(3,foodDetailsFile)
            foodDetails.append(row.replace("\n","").replace("_","").split(" | "))
        return removeEmptyList(foodDetails)

def readOrderRecordsFile():
    orderDetails = []
    with open('orderRecords.txt', mode='r') as orderRecordsFile:
        skipFileLine(6,orderRecordsFile)
        for line in orderRecordsFile:
            orderDetails.append(line.strip('\n').split(" | "))
    return orderDetails

'''DECLARING FUNCTIONS THAT CAN BE USED ANYWHERE IN THE PROGRAM'''

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

def userInput(inputString, skipLine): #Function to accept input from user
    if (skipLine):
        return input("\n{} >> ".format(inputString))
    else:
        return input("{} >> ".format(inputString))

def authUsername(username,filename):
    userExistsCount = 0
    for data in filename:
        userExistsCount += data.count(username.lower())
    if userExistsCount > 0:
        print(" Username found, please enter password\n")
        return True
    return False

def authPassword(password,filename):
    passwordExistsCount = 0
    for data in filename:
        passwordExistsCount += data.count(password)
    if passwordExistsCount > 0:
        progressBar("Logging you in")
        time.sleep(0.05)
        return True
    return False 

def skipFileLine(count,filename) : 
        for _ in range(count):
            next(filename)

def removeEmptyList(list):
    for data in list:
        while ('' in data):
            data.remove('')
            new_list = [i for i in list if i != []]
    return new_list

def progressBar(loadingMessage):
    print('{}...'.format(loadingMessage))
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.05)
        print("\r" + animation[i],end="")

'''DECLARING FUNCTIONS FOR ADMIN DASHBOARD'''
'''Login to access system'''
def adminLoginPage(): #Main Admin Login Page
    print("\nAdmin Authentication Section")
    print("-" * 28)
    uName = input("Username: ")
    progressBar("Checking if username exists")
    time.sleep(0.05)
    if (authUsername(uName,readAdminDetailsFile())):
        while True:
            if (authPassword(input("Password: "),readAdminDetailsFile())):
                adminMenu(uName)
                break
            else:
                print("Incorrect password, please retry\n")      
    else:
        print("Username not found, please retry\n")
        time.sleep(1)
        clearConsole()
        adminLoginPage()

def adminMenu(uName): #Admin Menu shown upon sucessful login
    clearConsole()
    print("Welcome {}, what would you like to do today?\n".format(uName))
    print("1. Add food item","2. Modify food item","3. Display records","4. Search record","0. Back to Main Menu", sep='\n')  
    input = userInput("I would like to",True)
    if input == "1" :
        foodCategoriesMenu()
    elif input == "2" :
        modifyFoodItemMenu()
    elif input == "3" :
        displayRecordsMenu()
    elif input == "4" :
        searchMainPage()
    elif input == "0" :
        main()
    else :
        invalidInput()

'''Add food item by category'''
def displayFoodCategories(): #Retrieve food categories from extractFoodCategories function
    count=1
    while (count<len(extractFoodCategories())):
        for list in extractFoodCategories():
            print("{}. {}".format(count,list))
            count+=1

def extractFoodCategories():
    originalList = readFoodDetailsFile()
    foodMenuList=[]
    for data in originalList:
        if data[0] not in foodMenuList:
            foodMenuList.append(data[0])
    return foodMenuList

def foodCategoriesMenu(): #Prompts admin to select which category of food item they want to add or to add new category 
    print("You have chosen to add food item by category","Choose one category\n",sep="\n")
    displayFoodCategories()
    print("0. Add new food Category")
    userSelection = userInput("Food Category",True)
    if int(userSelection) == 0:
        categoryName = userInput("Category Name",False)
        categoryDescription = userInput("Description",False)
        addFoodCategory(categoryName,categoryDescription)
    else: 
        addFoodItem((extractFoodCategories()[int(userSelection)-1]))

def addFoodCategory(name,description): #Adds new food category in foodDetails.txt file
    uppercaseName = name.upper()
    capitalizeDescription = description.capitalize()
    with open('foodDetails.txt','a') as foodDetailsFile:
            foodDetailsFile.write('\n' + '_'*88 + '\n\n')
            foodDetailsFile.write("{} - {}".format(uppercaseName,capitalizeDescription) + '\n')
            foodDetailsFile.write("_"*88 + '\n')

def addFoodItem(chosenFoodCategory): #Still in progress
    try:
        foodItemName = userInput("Food Item Name",False)
        foodItemDetails = userInput("Food Item Details",False)
        foodItemPrice = float(userInput("Food Item Price",False))
    except ValueError: 
        print("Please enter the correct value")
    clearConsole()
    print("Please confirm if these are the details you would like to add")
    print("""=====================
| FOOD CATEGORY     | {}
| FOOD ITEM NAME    | {}
| FOOD ITEM DETAILS | {}
| FOOD ITEM PRICE   | {}
=====================""".format(chosenFoodCategory,foodItemName,foodItemDetails,foodItemPrice))
    if (userInput("(Y)es/(N)o")=="Y|y"):
        pass

'''Modify food item'''
def modifyFoodItemMenu():
    clearConsole()
    print("\nPlease select any option below.")
    print("1. Remove Food Item","2. Edit Food Item","3. Back to Main Menu","0. Back",sep='\n')
    input = userInput("Option",True)
    if input == "1" :
        removeFoodItem()
    elif input == "2" :
        editFoodItem()
    elif input == "3" :
        main()
    elif input == "0" :
        adminMenu()
    else :
        invalidInput()

def removeFoodItem() : pass
def editFoodItem() : pass
def removeCategory() : pass
def editCategory() :pass

'''Display records of food category'''
def displayRecordsMenu(): #Dispaly records main page
    print("Records Display Page")
    print("1. Food Categories","2. Food Items by Category","3. Customer Orders","4. Customer Payment","0. Back to Admin  Menu", sep='\n')  
    input = userInput("Display all records of",True)
    if input == "1" :
        displayFoodCategoryRecords()
    elif input == "2" :
        displayFoodItemRecords()
    elif input == "3" :
        displayOrderRecords()
    elif input == "4" :
        displayPaymentRecords()
    elif input == "0" :
        adminMenu()
    else :
        invalidInput()

def displayFoodCategoryRecords():
    foodCategoryDetails = []

    '''Extract main category and descriptions and appends to list'''
    raw_list = []
    with open ('foodDetails.txt', mode='r') as foodDetailsFile:
        skipFileLine(2,foodDetailsFile)
        for line in foodDetailsFile:
            raw_list.append(line.strip().replace('_','').split(","))
        for data in removeEmptyList(raw_list):
            if (" | " in data[0]):
                index = raw_list.index(data)
                raw_list.pop(index)
    foodCategoryLists = [i for i in raw_list if i != []]

    '''Split food category and descriptions to 2 separate variables'''
    for list in foodCategoryLists:
        for data in list:
            for i in range(len(data)):
                if data[i] == "-":
                    foodCategoryDetails.append([''.join(data[0:i-1]), ''.join(data[i+2:-1])])            
    
    '''Print data in user readable form'''
    print("""\t\tDETAILS OF FOOD CATEGORIES
\t\t--------------------------""")
    print("""CATEGORY NAME(S)\t\tCATEGORY DESCRIPTION(S)
---------------\t\t\t----------------------""")
    for data in foodCategoryDetails:
        print('{:<32}{}'.format(data[0],data[1]))

'''Display records of food items by category'''
def displayFoodItemRecords():
    print("You have selected to display food items by category")
    print("Select the food category that you want to be displayed")
    displayFoodCategories()
    chosenCategory = userInput("Food category",True)
    print("Generating report...")
    time.sleep(1)
    print("""REPORT OF FOOD ITEMS IN {} FOOD CATEGORY
-----------------------------------------------""".format(extractFoodCategories()[int(chosenCategory)-1]).upper())
    print("""FOOD ITEM ID\tFOOD ITEM PRICE\t FOOD ITEM NAME
-----------------------------------------------""")
    for data in readFoodDetailsFile():
        if (extractFoodCategories()[int(chosenCategory)-1]) in data[0]:
            print('{:<16}{:<15}\t {}'.format(data[1],data[3],data[2]))

'''Display Records of Customer Orders'''
def displayOrderRecords():
    print("""\n\t\t\t\tREPORT OF ALL CUSTOMER ORDERS
\t\t\t\t-----------------------------\n""")
    print("""CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)
-----------------       --------        -------------   ------------    -----------------""")
    for data in readOrderRecordsFile():
        print('{:<24}{:<16}{:<16}{:<16}{}'.format(data[0],data[1],data[3],data[7],data[2]))

'''Display Records of Customer Payments'''
def displayPaymentRecords():
    print("""\n\t\t\t\tREPORT OF ALL CUSTOMER PAYMENTS
\t\t\t\t-------------------------------\n""")
    print("""CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\tPAID ON
-----------------       --------        -------------   ------------    --------------  -------""")
    for data in readOrderRecordsFile():
        print('{:<24}{:<16}{:<16}{:<16}{:<16}{}'.format(data[0],data[1],data[3],data[4],data[5],data[6]))

'''Search Specific Customer Order Record'''
def searchMainPage():
    clearConsole()
    print("_____________".center(50))
    print("""
                  SEARCH RECORD""")
    print("_____________".center(50))
    print("\n1. CUSTOMER ORDER RECORD\t2. CUSTOMER PAYMENT RECORD".center(50))
    print("\nWhich record do you want to check?")
    while (True):
        try:
            searchCategory = int(userInput("Input 1 or 2",False))
            if searchCategory == 1:
                searchCustomerOrder()
            elif searchCategory == 2:
                searchCustomerPayment()
            else:
                print("The number you submitted is outside the allowed range!")
            break
        except ValueError:
            print("Please enter a number!")





def searchCustomerOrder():
    clearConsole()
    print("_____________________".center(50))
    print("""
              CUSTOMER ORDER RECORD""")
    print("_____________________".center(50))
    print("""\n{}1. CUSTOMER USERNAME\t2. ORDER ID""".format(" "*4))
    print("\nOn what basis should the records be searched?".center(100))
    while (True):
        try:
            orderList = readOrderRecordsFile()
            searchCriteria = int(userInput("Input 1 or 2",False))
            if (searchCriteria == 1) :
                recordByUsername = []
                username = userInput("Please enter Customer Username",True)
                count = 0
                for data in orderList:
                    if (username.lower() == data[0]):
                        recordByUsername.append([data[1],data[2],data[3],data[7]])
                        count+=1
                if count >=1:
                    print("{} order records have been found for {}".format(count,username))
                    progressBar("Generating report")
                    time.sleep(0.5)
                    print("""\n\t\t\t\tORDER REPORT FOR {}
\t\t\t\t-----------------{}\n""".format(username.upper(),"-"*len(username)))
                    print("""CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)
-----------------       --------        -------------   ------------    -----------------""")
                    for data in recordByUsername:
                        print('{:<24}{:<16}{:<16}{:<16}{}'.format(username.upper(),data[0],data[2],data[3],data[1]))
                else:
                    print("No order records found for {}".format(username))
                break
            if (searchCriteria == 2):
                orderID = userInput("Please enter Order ID",True)
                recordById = []
                orderExists = False
                for data in orderList:
                    if (orderID.upper() == data[1]):
                        recordById.append([data[0],data[1],data[2],data[3],data[7]])
                        orderExists = True
                if (orderExists):
                    print("1 Order record have been found for Order ID {}".format(orderID.upper()))
                    progressBar("Generating report")
                    time.sleep(0.5)
                    print("""\n\t\t\t\tORDER REPORT FOR {}
\t\t\t\t-----------------{}\n""".format(orderID.upper(),"-"*len(orderID)))
                    print("""CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)
-----------------       --------        -------------   ------------    -----------------""")
                    for data in recordById:
                        print('{:<24}{:<16}{:<16}{:<16}{}'.format(data[0].upper(),data[1],data[3],data[4],data[2]))
                else:
                    print("No order records found for {}".format(orderID.upper()))
                break
            else:
                print("The number you submitted is outside the allowed range!")
                time.sleep(1)
        except ValueError:
            print("Please submit a number")
            time.sleep(1.5)
    


def searchCustomerPayment():pass

'''Search Specific Customer Payment Record'''

'''DECLARING FUNCTIONS FOR GUEST DASHBOARD'''
def guestMenu(): #Guest Dashboard Main Page
    clearConsole()
    print("Please select any option below.")
    print("1. View Menu","2. Customer Login", "3. New Customer Registration", "4. Back to Main Menu", sep='\n')
    input = userInput("Choice",True)
    if input == "1":
        viewCategoryList()
    elif input == "2":
        authenticateCustomer()
    elif input == "3":
        customerRegistration()
    elif input == "4":
        mainMenu()
    else:
        invalidInput()
        guestMenu()
'''View all food items as per category'''
'''New customer registration to access other details'''

'''DECLARING FUNCTIONS FOR REGISTERED CUSTOMER DASHBOARD'''
'''Login to access system'''
def regCustomerMenu(): #Customer menu upon successful login
    clearConsole()
    print("Welcome {}!, what would you like to do today?")
    print("1. View Item List", "2. View Item Details", "3. Add Food to Cart", "4. Checkout", "5. Main Menu", sep='\n')
    input = userInput("Choice",True)
    if input == "1":
        viewItemList()
    elif input =="2":
        viewItemDetail()
    elif input == "3":
        addFoodToCart()
    elif input =="4":
        checkout()
    elif input == "5":
        mainMenu()
    else:
        invalidInput()
        regCustomerMenu()

'''View detail of food category'''
'''View detail of food items'''
'''Select food item and add to cart'''
'''Do payment to confirm order'''

'''DECLARING MAIN GREETING PAGE'''
def main():
    clearConsole()
    print("Welcome to Spiderman Online Food Service!")
    time.sleep(1)
    print("Please select any option below.", "1. Admin", "2. Customer", "3. Quit Program", sep=' \n')
    while (True):
        try:
            input = int(userInput("Login to",True))
            if input == 1 :
                adminLoginPage()
            elif input == 2 :
                guestMenu() 
            elif input== 3 :
                quit()
            else:
                print("Out of range, please enter a number between 1 and 3")
                time.sleep(1)
            break
        except ValueError:
            print("You entered an alphabet, please enter a number between 1 and 3")
            time.sleep(1)
            

'''EXECUTE MAIN'''
main()


'''Empty functions'''

def order() :
    clearConsole()
    print("\nPlease select any option below.")
    print("1. Cancel an order","2. Back to Main Menu","0. Back",sep='\n')
    input = userInput("Choice",True)
    if input == "1" : 
        cancelOrder() 
    elif input == "2" :
        main()
    elif input == "0" :
        adminMenu()
    else : 
        invalidInput()
        order()
def cancelOrder() : pass
def checkPayment() : pass
def viewCategoryList() : pass
def viewItemList() : pass
def registered() : pass
def viewItemDetail() : pass
def viewCategoryDetail() : pass
def addFoodToCart() : pass
def checkout() : pass
def logout() : pass
def customerRegistration() : pass 
