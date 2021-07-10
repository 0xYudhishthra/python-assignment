#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

#!/usr/bin/env python3
import os
import time
'''
These functions can be used across any part of the program
'''

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
        print("Username found, please enter password\n")
        return True
    return False

def authPassword(password,filename):
    passwordExistsCount = 0
    for data in filename:
        passwordExistsCount += data.count(password)
    if passwordExistsCount > 0:
        print("Logging you in...")
        time.sleep(1)
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



'''
Functions for Admin Dashboard
0. Login to Access System
1. Add food item by category
2. Modify food item (Edit, Delete, Update)
3. Display Records of Food Category ( )
4. Display Records of Food Items by Category
5. Display Records of Customer Orders
6. Display Records of Customer Payments
7. Search Specific Customer Order Record
8. Search Specific Customer Payment Record
9. Exit
'''
#Login to Access System 
def readAdminDetailsFile(): #Reads admin file and converts it to list
    with open ('adminDetails.txt', mode='r') as admin_file:
        admin_list = []
        for _ in range(1):
                next(admin_file)
        for row in admin_file:
            adminDetails=row.strip("\n").replace(" | "," ").split(" ")
            admin_list.append(adminDetails)
        return admin_list

def adminLoginPage():
    print("\nAdmin Authentication Section")
    print("-" * 28)
    uName = input("Username: ")
    print("Checking if username exists...")
    time.sleep(1)
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

def adminMenu(uName) :
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
        searchRecordMenu()
    elif input == "0" :
        mainMenu()
    else :
        invalidInput()


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
        mainMenu()
    elif input == "0" :
        adminMenu()
    else :
        invalidInput()


#Add Food Item by category
def readFoodItemDetails(): #Function to convert foodDetails text file to list

    foodDetails=[]
    with open ('foodDetails.txt', mode='r') as foodDetailsFile:
        skipFileLine(2,foodDetailsFile) 
        for row in foodDetailsFile:
            if row.startswith("_"):
                skipFileLine(3,foodDetailsFile)
            foodDetails.append(row.replace("\n","").replace("_","").split(" | "))
        return removeEmptyList(foodDetails)

def extractFoodCategories():
    originalList = readFoodItemDetails()
    foodMenuList=[]
    for data in originalList:
        if data[0] not in foodMenuList:
            foodMenuList.append(data[0])
    return foodMenuList

def displayFoodCategories():
    count=1
    while (count<len(extractFoodCategories())):
        for list in extractFoodCategories():
            print("{}. {}".format(count,list))
            count+=1
    
def foodCategoriesMenu() : 
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

def addFoodCategory(name,description):
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
        writeFoodDetailsToFile()

def writeFoodDetailsToFile():
    with open ('foodDetails.txt','a') as foodDetailsFile:
         for row in foodDetailsFile:
             print(row)      



#Display records main page
def displayRecordsMenu():
    print("Records Display Page")
    print("1. Food Categories","2. Food Items by Category","3. Customer Orders","4. Customer Payment","0. Back to Admin  Menu", sep='\n')  
    input = userInput("Display all records of",True)
    if input == "1" :
        displayFoodCategoryRecords()
    elif input == "2" :
        displayFoodItemRecords()
    elif input == "3" :
        displayCustomerOrderRecords()
    elif input == "4" :
        displayCustomerPaymentRecords()
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
                    #foodCategoryDescription.append(''.join(data[i+2:-1]))              
    '''Print data in user readable form'''

    print ("""
==================   =========================          
FOOD CATEGORY NAME   FOOD CATEGORY DESCRIPTION
==================   =========================
""")
    for data in foodCategoryDetails:
        print("{} {}".format(data[0],data[1]))



def removeCategory() : pass
def editCategory() :pass


    


def removeFoodItem() : pass
def editFoodItem() : pass

def order() :
    clearConsole()
    print("\nPlease select any option below.")
    print("1. Cancel an order","2. Back to Main Menu","0. Back",sep='\n')
    input = userInput("Choice",True)
    if input == "1" : 
        cancelOrder() 
    elif input == "2" :
        mainMenu()
    elif input == "0" :
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
        customerMenu()

def regCustomerMenu():
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

def viewCategoryList() : pass
def viewItemList() : pass
def registered() : pass
def viewItemDetail() : pass
def viewCategoryDetail() : pass
def addFoodToCart() : pass
def checkout() : pass

def authenticateCustomer() : pass
def logout() : pass
def createFile() : pass
def deleteFile() : pass
def readFile() : pass
def writeFile() : pass

'''
Functionalities for Guest Dashboard
0. View all food items as per category
1. New customer registration to access other details
2. Exit
'''

def guestMenu():pass
def viewFoodItem():pass
def customerRegistration() : pass 

'''
Functionalities for Registered Customer Dashboard
0. Login to access system
1. View detail of food category
2. View detail of food items
3. Select food item and add to cart
4. Do payment to confirm order
5. Exit
'''




def mainMenu():
    print("Please select any option below.", "1. Admin", "2. Customer", "3. Quit Program", sep=' \n')
    input = userInput("Login to",True)
    if input == "1" :
        adminLoginPage()
    elif input == "2" :
        customerMenu() 
    elif input== "3" :
        quit()
    else :
        invalidInput()
        mainMenu()

def main() :
    clearConsole()
    print("Welcome to Spiderman Online Food Service!")
    time.sleep(1)
    mainMenu()

main()
