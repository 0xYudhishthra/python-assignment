#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

#!/usr/bin/env python3

'''IMPORTING NECESSARY EXTERNAL MODULES'''
import os
import time
from typing import Type

'''LOCATION OF FILES WITH ADMIN, FOODS AND CUSTOMER'S DETAILS'''
FOOD_DETAILS_FILE = "./foodDetails.txt"
CUSTOMER_DETAILS_FILE = "./customerDetails.txt"
ADMIN_DETAILS_FILE = "./adminDetails.txt"
ORDER_RECORDS_FILE = "./orderRecords.txt"

'''UTILITY FUNCTIONS'''
def clearConsole(): #Function to clear all existing text in console
    if (os.name in ("nt", "dos")):  
        os.system("cls")
    else:
        os.system("clear")

def quit() : #Exits program cleanly
    print("\n")
    print(f' {"Thank you! Please come again"} '.center(85, '='))   
    time.sleep(1)
    exit()

def userInput(promptMessage:str, skipLine:bool) -> input: #Function to format prompt message to accept input from users 
    if (skipLine):
        return input(f"\n{promptMessage} >> ")
    else:   
        return input(f"{promptMessage} >> ")

def authUsername(username:str, detailsList:list) -> bool:  #Verifies if username exists in the respective list 
    for data in detailsList:
        if username == data[0]:
            return True

def authPassword(username:str, password:str, detailsList:list) -> bool:  #Verifies if password exists in the respective list
    for data in detailsList:
        if username == data[0] and password == data[1]:
            return True

def skipFileLine(count:int,fileHandle): #Skips n number of lines in a file handle (textIOWrapper) that is being read/write 
        for _ in range(count):
            next(fileHandle)

def removeEmptyList(sourceList:list) -> list: #Removes list with empty strings and lists with no elements
    for data in sourceList:
        while ('' in data):
            data.remove('')
    return [data for data in sourceList if data != []]

def progressBar(loadingMessage:str): #Displays loading animation with message
    print(f'{loadingMessage}...')
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for item in animation:
        time.sleep(0.05)
        print("\r" + item, end="")

def pageBanners(pageTitle:str,centerLength:int): #Displays banner for each different pages for respective dashboards
    print(f'{"_"*(len(pageTitle))}\n'.center(centerLength))
    print(f'{pageTitle}'.center(centerLength))
    print(f'{"_"*len(pageTitle)}'.center(centerLength))

'''DECLARING FUNCTIONS FOR ADMIN DASHBOARD'''
'''Login to access system'''
def readAdminDetailsFile() -> list: #Reads file with admin details, extracts username and passwords without headers and appends it to list, PSEUDOCODE TBC
    adminDetailsList = [] 
    try:
        with open (ADMIN_DETAILS_FILE,mode='r') as adminDetailsFile:
            skipFileLine(6,adminDetailsFile)
            for row in adminDetailsFile:
                adminDetailsList.append(row.strip("\n").replace(" | "," ").split(" "))
        if adminDetailsList == [] : raise UnboundLocalError
    except FileNotFoundError:
        print("\nERROR: Admin details file is missing!")
        exit()
    except UnboundLocalError:
        print("\nERROR: No data in Admin details file!")
        exit()
    return adminDetailsList

def adminLoginPage(): #Login Page for SOFS adminstrators, TO-DO: show message when user enter without submitting anything
    adminDetailsList = readAdminDetailsFile()
    usernameExists = False
    while(not usernameExists):
        uName = userInput("Username",True).lower()
        if uName == "" : continue
        progressBar("Authenticating username")
        time.sleep(0.05)
        usernameExists = authUsername(uName,adminDetailsList)
        if (usernameExists):
            print(" Username found, please enter password\n")
        else:
            print(" ERROR: Username not found, please retry\n")
    while (usernameExists):
        uPass = userInput("Password",True)
        if uPass == "" : continue
        progressBar("Authenticating password")
        time.sleep(0.05)
        passwordMatch = authPassword(uName, uPass,adminDetailsList)
        if (passwordMatch):
            adminMenu(uName)
            break  
        else: 
            print(" ERROR: Incorrect password , please retry")

def adminMenu(uName:str="admin"): #Admin Menu shown upon successful login, PSEUDOCODE TO BE CHANGED
    CHOICES = [[1, "ADD NEW FOOD ITEM", addFoodItemMenu], [2, "MODIFY FOOD ITEM", modifyFoodItemMenu], 
               [3, "DISPLAY RECORDS", displayRecordsMenu], [4, "SEARCH RECORDS", searchRecordsMenu]]
    clearConsole()
    pageBanners("ADMIN DASHBOARD",50)
    print(f'\nHey, {uName.capitalize()}! What would you like to do today?\n')
    print("1. Add food item","2. Modify food item","3. Display records","4. Search record","0. Log out", sep='\n')
    while True:
        try:
            userSelection = int(userInput("I would like to",True))
            if userSelection == 0:
                progressBar("Logging out")
                main()
            elif userSelection > len(CHOICES):
                print("Number is out of range!")
                time.sleep(1)
                continue
            for choice in CHOICES:
                if userSelection == choice[0]:
                    clearConsole()
                    pageBanners(choice[1],50)
                    choice[2]()
            break
        except ValueError:
            print("Please submit a number")
            time.sleep(1) 

'''Add food item by category'''
def readFoodDetailsFile() -> list: #Reads file with food details, extract food details without headers and appends it to list, TO-DO: modify try-catch to fit missing files
    foodDetailsList=[]
    try:
        with open (FOOD_DETAILS_FILE, mode='r') as foodDetailsFile:
            skipFileLine(6,foodDetailsFile) 
            for row in foodDetailsFile:
                if row[0] == "_":
                    skipFileLine(3,foodDetailsFile)
                foodDetailsList.append(row.replace("\n","").replace("_","").split(" | "))
        if foodDetailsList == [] : raise UnboundLocalError
    except FileNotFoundError:
        print("\nERROR: Food details file is missing!")
        exit()
    except UnboundLocalError:
        print("\nERROR: No data in food details file!")
        exit()
    return removeEmptyList(foodDetailsList)

def displayFoodCategories(): #Displays list of food categories ONLY as ordered list, update pseudocode
        try:  
            foodCategoriesList = extractFoodCategories()
            for list in foodCategoriesList:
                print(f'{foodCategoriesList.index(list)+1}. {list[0].capitalize()}')
        except TypeError:
            print("Food details file is corrupted!")

def addFoodItemMenu(): #Prompts admin to select which category of food item they want to add or to add new food category, PSEUDOCODE TO BE CHANGED
    while True:
        try:
            foodCategoryTitles = extractFoodCategories()
            print(f"\nIn which category would you like to add the food item?\n\n")
            displayFoodCategories()
            print(f"{len(foodCategoryTitles)+1}. Add new food category")
            print(f"\n0. Back to main menu")
            chosenFoodCategoryNumber = int(userInput("Food Category Number",True))
            if (chosenFoodCategoryNumber == len(foodCategoryTitles)+1): 
                newFoodCategoryName = userInput("Category Name",False)
                newFoodCategoryDescription = userInput("Description",False)
                writeNewFoodCategoryToFile(newFoodCategoryName,newFoodCategoryDescription)
                print(f"Would you like to add a new food item in this category?")
                userConfirmation = userInput("(Y)es/(N)o",False).upper()
                if userConfirmation == 'Y':
                    foodItemName,foodItemPrice = getNewFoodItemDetails(newFoodCategoryName)
                    writeNewFoodItemToFile(newFoodCategoryName, foodItemName, foodItemPrice)
                else:
                    addFoodItemMenu()
            elif (chosenFoodCategoryNumber > 0 and chosenFoodCategoryNumber <= len(foodCategoryTitles)): 
                chosenFoodCategoryName = foodCategoryTitles[int(chosenFoodCategoryNumber)-1][0].replace("FOOD CATEGORY","").strip().capitalize()
                foodItemName,foodItemPrice = getNewFoodItemDetails(chosenFoodCategoryName)
                print("\nPlease confirm the new food details you would like to add")
                userConfirmation = userInput("(Y)es/(N)o",False).upper()
                if (userConfirmation == 'Y'):
                    writeNewFoodItemToFile(chosenFoodCategoryName,foodItemName,foodItemPrice)
                elif (userConfirmation == 'N'):
                    addFoodItemMenu()
                else:
                    print("Please enter either Y or N")
                    continue
            elif chosenFoodCategoryNumber == 0:
                adminMenu()
            else:
                print("Invalid food category number")
                time.sleep(1)
                continue
            break
        except ValueError:
            print("Please submit a number!")
            time.sleep(1)
        except TypeError:
            print("Food details file is corrupted!")
            break

def getNewFoodItemDetails(chosenFoodCategoryName:str) -> str: #Gets details of new food item details from user
        try:
            foodItemName = userInput("New Food Item Name",False)
            foodItemPrice = format(float(userInput("New Food Item Price",False)),".2f")
            print(f"\nFOOD CATEGORY\tFOOD ITEM PRICE\t FOOD ITEM NAME\n{'-'*13}{' '*3}{'-'*15}{' '*2}{'-'*14}")
            print('{:<16}{:<17}{}'.format(chosenFoodCategoryName,foodItemPrice,foodItemName))  
            return foodItemName,foodItemPrice
        except ValueError:
            print("Invalid value entered")

def writeNewFoodCategoryToFile(categoryName:str,categoryDescription:str): #Adds new food category in food details file
    uppercaseName = categoryName.upper()
    capitalizedDescription = categoryDescription.capitalize()
    with open(FOOD_DETAILS_FILE,'a') as foodDetailsFile:
            foodDetailsFile.write('\n' + '_'*88 + '\n\n')
            foodDetailsFile.write(f"{uppercaseName} FOOD CATEGORY - {capitalizedDescription}\n")
            foodDetailsFile.write("_"*88)

def writeNewFoodItemToFile(foodCategoryName:str,foodItemName:str,foodItemPrice:float): #Directly writes new food item data to food details file
    try:
        orderRecordsList = []
        with open (FOOD_DETAILS_FILE, mode='r') as f:
            for row in f:   
                orderRecordsList.append([row])
        foodItemIndexes = [
            orderRecordsList.index(data)
            for data in orderRecordsList
            if foodCategoryName in data[0]
        ]
        if not foodItemIndexes:
            newFoodID = foodCategoryName[0] + '1'
            lastFoodItemIndex = (len(orderRecordsList)-1)
        else: 
            lastFoodItemIndex = foodItemIndexes[-1]
            lastFoodItemRecord = orderRecordsList[lastFoodItemIndex][0].split(" | ")
            newFoodID = lastFoodItemRecord[0][0] + str(int(lastFoodItemRecord[1].strip(lastFoodItemRecord[0][0]))+1)
        if (lastFoodItemIndex == (len(orderRecordsList)-1)):
            orderRecordsList.insert(lastFoodItemIndex+1, [f'\n{foodCategoryName} | {newFoodID} | {foodItemName} | {foodItemPrice}'])
        else:
            orderRecordsList.insert(lastFoodItemIndex+1, [f'{foodCategoryName} | {newFoodID} | {foodItemName} | {foodItemPrice}\n'])
        with open (FOOD_DETAILS_FILE, mode='w') as foodDetailsFile:
            for data in orderRecordsList:       
                foodDetailsFile.write(data[0])
    except TypeError:
        print("Food details text file is corrupted!")
    except FileNotFoundError:
        print("Food details text file is missing!")

'''Modify food item'''
def modifyFoodItemMenu(): #Main page for admins to modify records of food items
    foodDetailsList = []
    with open(FOOD_DETAILS_FILE,mode='r') as foodDetailsFile:
        for row in foodDetailsFile:
            foodDetailsList.append([row])
    print("\n{}1. UPDATE RECORD\t2. DELETE RECORD".format(" "*5))
    print("\nWhat would you like to do?")
    while (True):
        try:
            modifyChoice = int(userInput("Input 1 or 2",False))
            if modifyChoice == 1:
                clearConsole()
                pageBanners("UPDATE FOOD ITEM",50)
                updateFoodItemMenu(foodDetailsList)
            elif modifyChoice == 2:
                clearConsole()
                pageBanners("DELETE FOOD ITEM",50)
                deleteFoodItemMenu(foodDetailsList)
            else:
                print("Number is out of range")
                continue
            break
        except ValueError:
            print("Please submit a number")

def verifyFoodItemId(foodItemId:str, foodDetailsList:list) -> bool: #Verifies the format and existence of the food item ID that has been received by the user
    if foodItemId == '' : 
        return False
    elif (foodItemId[0].isalpha() and foodItemId[1 : len(foodItemId)].isdigit()):
        for data in foodDetailsList:
            if foodItemId in data[0]:
                return True
    else:
        return False

def listOutFoodItems(chosenFoodCategoryName:str): #Displays the details of all food items in the food details file based on the category chosen by the user
    while True:
        try:
            progressBar("Retrieving food item records")
            time.sleep(0.5)
            print(f"\n\nREPORT OF FOOD ITEMS IN {chosenFoodCategoryName.upper()}\n{'-'*24}{'-'*len(chosenFoodCategoryName)}")
            print(f"FOOD ITEM ID\tFOOD ITEM PRICE\t FOOD ITEM NAME\n{'-'*12}{' '*4}{'-'*15}{' '*2}{'-'*14}")
            for data in readFoodDetailsFile():
                if (chosenFoodCategoryName.replace("FOOD CATEGORY", "").strip().capitalize()) in data:
                    print('{:<16}{:<15}\t {}'.format(data[1],data[3],data[2]))
            break
        except TypeError:
            print("Please enter a number")

def updateFoodItemMenu(foodDetailsList): #Menu for user to choose which specific food item id they want to update
    while True:
        try:
            foodCategoryTitles = extractFoodCategories()
            print("\nIn which category would you like to update the food item?")
            displayFoodCategories()
            categoryNumber = int(userInput("Category number",True))
            if 0 < categoryNumber <= len(foodCategoryTitles):
                listOutFoodItems(foodCategoryTitles[categoryNumber-1][0])  
                foodItemId = userInput("Enter the Food Item ID that you would like to update",True).upper()
                if (verifyFoodItemId(foodItemId, foodDetailsList)):
                    print(f"Food item ID selected: {foodItemId}")
                    for data in foodDetailsList:
                        if foodItemId in data[0]:
                            foodItemIdList = data[0].split(" | ")
                            foodItemIdIndex = foodDetailsList.index(data)              
                    updateFoodItemRecord(foodDetailsList, foodItemIdList, foodItemIdIndex)
                    break
                else:
                    print("Invalid Food Item ID")
            else:
                print("Number is out of range")
        except ValueError:
            print("Please submit a number")
            continue

def deleteFoodItemMenu(foodDetailsList): #Menu for user to choose which specific food item id they want to delete
    while True:
        try: 
            foodCategoryTitles = extractFoodCategories()
            print("\nIn which category would you like to delete the food item?")
            displayFoodCategories()
            categoryNumber = int(userInput("Category number",True))
            if 0 < categoryNumber <= len(foodCategoryTitles):
                listOutFoodItems(foodCategoryTitles[categoryNumber-1][0])
                foodItemId = userInput("Enter the Food Item ID that you would like to delete",True).upper()
                if(verifyFoodItemId(foodItemId,foodDetailsList)):
                    print(f"Are you sure you want to delete {foodItemId}?")
                    userConfirmation = userInput("(Y)es/(N)o",True).upper()
                    if (userConfirmation in ('Y', 'N')):
                        deleteFoodItemRecord(userConfirmation, foodItemId, foodDetailsList)
                        break
                    else:
                        print("Invalid input")
                else:
                    print("Invalid Food Item ID")
            else:
                print("Invalid Food Category Number")
        except ValueError:
            print("Please submit a number")

def updateFoodItemRecord(foodDetailsList, foodItemIdList, foodItemIdIndex): #Updates a specific record of food item in the food details text file
    try:
        print("\nWhat would you like to update?","1. Food Item Price","2. Food Item Name","3. Both",sep='\n')
        while True:
            updateCriteria = int(userInput("Update choice",True))
            if updateCriteria == 1:
                newPrice = float(userInput("New food item price",False))
                newPrice = format(newPrice,'.2f')
                foodItemIdList[3] = f'{newPrice}\n' if '\n' in foodItemIdList[3] else f'{newPrice}'
            elif updateCriteria == 2:
                foodItemIdList[2] = f'{userInput("New food item name",False)}'
            elif updateCriteria == 3:
                newPrice = userInput("New food item price",False)
                foodItemIdList[2] = f'{userInput("New food item name",False)}'
                foodItemIdList[3] = f'{newPrice}\n' if '\n' in foodItemIdList[3] else f'{newPrice}' 
            else:
                print("Number out of range")
                continue
            break     
    except FileNotFoundError:
        print("Food details file not found")
    except ValueError:
        print("Please submit a number")
    foodDetailsList[foodItemIdIndex] = [" | ".join(foodItemIdList)]
    with open (FOOD_DETAILS_FILE,mode='w') as f:
        for data in foodDetailsList:
            f.write(data[0])

def deleteFoodItemRecord(userConfirmation, foodItemId, foodDetailsList): #Deletes a specific food item record in the food details text file
    while True:
        try:
            if (userConfirmation=="Y"):
                for data in foodDetailsList:
                    if foodItemId in data[0]:
                        foodDetailsList.pop(foodDetailsList.index(data))
                    if '\n' in foodDetailsList[-1][-1]:
                        temp = foodDetailsList[-1][-1].strip("\n")
                        foodDetailsList[-1][-1] = temp
                with open (FOOD_DETAILS_FILE,mode='w') as f:
                    for data in foodDetailsList:
                        f.write(data[0])
                break
            else:
                adminMenu()
        except FileNotFoundError:
            print("Food details file is missing")
            

'''Main Menu Page for Display'''
def readOrderRecordsFile() -> list: #Reads file with order records, extract order records without headers and append to list
    orderDetailsList = []
    try:
        with open(ORDER_RECORDS_FILE, mode='r') as orderRecordsFile:
            skipFileLine(6,orderRecordsFile)
            for row in orderRecordsFile:
                orderDetailsList.append(row.strip('\n').split(" | "))
        return orderDetailsList
    except FileNotFoundError:
        print("Order records file is missing!")

def extractFoodCategories(): #Gets the title and description of the food categories ONLY from the food details text file and append it to list
    try:
        rawList = []
        foodCategoryDetails = []
        with open (FOOD_DETAILS_FILE, mode='r') as foodDetailsFile:
            skipFileLine(4,foodDetailsFile)
            for line in foodDetailsFile:
                rawList.append(line.strip().replace('_','').split(","))
        for data in removeEmptyList(rawList):
            if " | " in data[0]:
                rawList.pop(rawList.index(data))
        for list in removeEmptyList(rawList):
            for data in list:
                for i in range(len(data)):
                    if data[i] == "-":
                        foodCategoryDetails.append([''.join(data[0:i-1]),''.join(data[i+2:-1])])
        return foodCategoryDetails       
    except TypeError:
        print("Food details text file is corrupted!")
    except FileNotFoundError:
        print("Food details text file is missing!")

def displayRecordsMenu(): #Display records main page
    orderRecordsList = readOrderRecordsFile()
    foodCategoryList = extractFoodCategories()
    print("\n1. Food Categories","2. Food Items by Category","3. Customer Orders","4. Customer Payment","0. Back to Admin  Menu", sep='\n')  
    while True:
        try:
            userSelection = int(userInput("Display all records of",True))
            if userSelection == 1 :
                progressBar("Generating report")
                displayFoodCategoryRecords(foodCategoryList)
            elif userSelection == 2 :
                print("\nSelect the food category that you want to be displayed")
                displayFoodCategories()
                chosenCategory = int(userInput("Food category",True))
                listOutFoodItems((foodCategoryList[chosenCategory-1][0]))
            elif userSelection == 3 :
                progressBar("Generating report")
                displayOrderOrPaymentRecords('orders',orderRecordsList)
            elif userSelection== 4 :
                progressBar("Generating report")
                displayOrderOrPaymentRecords('payments',orderRecordsList)
            elif userSelection == 0 :
                adminMenu()
            else :
                print("Number out of range")
                continue
            break
        except ValueError:
            print("Please enter a number")

def displayFoodCategoryRecords(foodCategoryList): #Displays the records of food categories and descriptions cleanly
    '''Print data in user readable form'''
    print(f'\n\t\tDETAILS OF FOOD CATEGORIES\n\t\t{"-"*26}')
    print(f"CATEGORY NAME(S)\t\tCATEGORY DESCRIPTION(S)\n{'-'*15}\t\t\t{'-'*22}")
    for data in foodCategoryList:
        print('{:<32}{}'.format(data[0],data[1]))

def displayOrderOrPaymentRecords(displayChoice,orderRecordsList): #Displays either order or payment records based on parameters given 
    print(f"\n\t\t\t\tREPORT OF ALL CUSTOMER {displayChoice.upper()}\n\t\t\t\t{'-'*31}\n")
    if displayChoice == 'orders':
        print(f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID (QUANTITY)\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*12}{' '*4}{'-'*18}")
        for data in orderRecordsList:
            print('{:<24}{:<16}{:<16}{:<16}{}'.format(data[0],data[1],data[3],data[7],data[2]))
    else:
        print(f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\tPAID ON\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*14}{' '*2}{'-'*14}{' '*2}{'-'*7}")
        for data in orderRecordsList:
            print('{:<24}{:<16}{:<16}{:<16}{:<16}{}'.format(data[0],data[1],data[3],data[4],data[5],data[6]))

'''Search Menu Main Page'''
def searchPageHeader(section): #Standard header for search page 
    clearConsole()
    pageBanners(section, 50)
    print("""\n{}1. CUSTOMER USERNAME\t2. ORDER ID""".format(" "*4))
    print("\nOn what basis should the records be searched?".center(100))

def searchRecordsMenu(): #Main page for users to select type of record search
    print("\n1. CUSTOMER ORDER RECORD\t2. CUSTOMER PAYMENT RECORD".center(50))
    print("\nWhich record do you want to check?")
    while True:
        try:
            orderRecordsList = readOrderRecordsFile()
            searchCategory = int(userInput("Input 1 or 2",False))
            if searchCategory == 1:
                searchPageHeader("SEARCH CUSTOMER ORDER")
                searchCriteria = int(userInput("Input 1 or 2",False))
                if searchCriteria == 1:
                    searchOrderByUsername(orderRecordsList)
                elif searchCriteria == 2:
                    searchOrderById(orderRecordsList)
                else: 
                    print("Invalid input")
                    continue
            elif searchCategory == 2:
                searchPageHeader("SEARCH CUSTOMER PAYMENT")
                searchCriteria = int(userInput("Input 1 or 2",False))
                if searchCriteria == 1:
                    searchPaymentByUsername(orderRecordsList)
                elif searchCriteria == 2:
                    searchPaymentById(orderRecordsList)
                else: 
                    print("Invalid input")
                    continue
            else:
                print("The number you submitted is outside the allowed range!")
                continue
            break
        except ValueError:
            print("Please enter a number!")

'''Search Specific Customer Order Record'''
def searchOrderByUsername(orderRecordsList:list): #Search customer order by username
    try:
        recordByUsername = []
        username = userInput("Please enter Customer Username",True)
        count = 0
        for data in orderRecordsList:
            if (username.lower() == data[0]):
                recordByUsername.append([data[0],data[1],data[2],data[3],data[7]])
                count+=1
        if count >=1:
            print("{} order records have been found for {}".format(count,username))
            progressBar("Generating report")
            time.sleep(0.5)
            displaySearchResults('orders',username,recordByUsername)
        else:
            print("No order records found for {}".format(username)) 
    except ValueError:
        print("Invalid value submitted")

def searchOrderById(orderRecordsList:list): #Search customer order by Order ID
    orderID = userInput("Please enter Order ID",True)
    recordById = []
    orderExists = False
    for data in orderRecordsList:
        if (orderID.upper() == data[1]):
            recordById.append([data[0],data[1],data[2],data[3],data[7]])
            orderExists = True
    if (orderExists):
        print("1 Order record have been found for Order ID {}".format(orderID.upper()))
        progressBar("Generating report")
        time.sleep(0.5)
        displaySearchResults('orders',orderID,recordById)
    else:
        print("No order records found for {}".format(orderID.upper()))
    
'''Search Specific Customer Payment Record'''
def searchPaymentByUsername(paymentList:list): #Search customer order by Username
    try:
        recordByUsername = []
        username = userInput("Please enter Customer Username",True)
        count = 0
        for data in paymentList:
            if (username.lower() == data[0]):
                recordByUsername.append([data[0],data[1],data[3],data[4],data[5],data[6]])
                count+=1
        if count >=1:
            print("{} payment records have been found for {}".format(count,username))
            progressBar("Generating report")
            time.sleep(0.5)
            displaySearchResults('payments',username,recordByUsername)
        else:
            print("No payment records found for {}".format(username))
    except ValueError:
        print("Invalid value submitted")

def searchPaymentById(paymentList:list): #Search customer order by Order ID
    orderID = userInput("Please enter Order ID",True)
    recordById = []
    orderIdExists = False
    for data in paymentList:
        if (orderID.upper() == data[1]):
            recordById.append([data[0],data[1],data[3],data[4],data[5],data[6]])
            orderIdExists = True
    if (orderIdExists):
        print("1 payment record have been found for Order ID {}".format(orderID.upper()))
        progressBar("Generating report")
        time.sleep(0.5)
        displaySearchResults('payments',orderID,recordById)
    else:
        print("No payment records found for {}".format(orderID.upper()))

'''Display Search Results'''
def displaySearchResults(recordName:str,searchBasis:str,resultsList:list): #Gets search results from the earlier search functions and displays it cleanly
    if recordName == 'orders':
        print(f"\n\t\t\t\tORDER REPORT FOR {searchBasis.upper()}\n\t\t\t\t{'-' * len(searchBasis)}{'-'*17}\n")
        print(f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*12}{' '*4}{'-'*17}")
        for data in resultsList:
            print('{:<24}{:<16}{:<16}{:<16}{}'.format(data[0].upper(),data[1],data[3],data[4],data[2]))           
    else:
        print(f"\n\t\t\t\tPAYMENT REPORT FOR {searchBasis.upper()}\n\t\t\t\t{'-'*19}{'-' * len(searchBasis)}\n")
        print(f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\tPAID ON\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*14}{' '*2}{'-'*14}{' '*2}{'-'*7}")
        for data in resultsList:
            print('{:<24}{:<16}{:<16}{:<16}{:<16}{}'.format(data[0].upper(),data[1],data[2],data[3],data[4],data[5]))  


'''DECLARING FUNCTIONS FOR GUEST DASHBOARD'''
def guestMenu(): #Guest Dashboard Main Page
    while True:
        clearConsole()
        pageBanners("GUEST DASHBOARD", 50)
        print("\nPlease select any option below.")
        print("1. View Menu","2. Customer Login", "3. New Customer Registration", "\n0. Back to Main Menu", sep='\n')
        input = userInput("Choice",True)
        if input == "1":
            viewCategoryList()
        elif input == "2":
            customerLoginPage()
            regCustomerMenu()
        elif input == "3":
            pageBanners("NEW ACCOUNT",50)
            customerRegistration()
        elif input == "0":
            break
        else:
            # invalidInput()
            guestMenu()
        
'''View all food items as per category'''
def viewCategoryList() :
    while True:
        clearConsole()
        pageBanners("MENU CATEGORIES",50)
        print("\n")
        displayFoodCategories()
        print("\n0. Back To Guest Menu")
        try:
            print("\nSelect the food category that you want to be displayed")
            chosenCategory = int(userInput("Food category",True))
            if chosenCategory == 0 :
                break
            elif chosenCategory <= 4 :
                listOutFoodItemsNoDetails((extractFoodCategories()[chosenCategory-1][0]))
            else :
                print("\nNumber out of range!")
                time.sleep(1.5)
                viewCategoryList()
        except ValueError:
            print("\nPlease enter a number!")
            time.sleep(1.5)
            viewCategoryList()

'''List out food items without details (Price and Descriptions)'''
def listOutFoodItemsNoDetails(chosenFoodCategoryName): #Displays the details of all food items in the food details file based on the category chosen by the user
    clearConsole()
    while True:
        try:
            progressBar("Retrieving food item menu")
            time.sleep(0.5)
            clearConsole()
            print(f"FOOD ITEMS IN {chosenFoodCategoryName.upper()}\n{'-'*24}{'-'*len(chosenFoodCategoryName)}")
            for data in readFoodDetailsFile():
                if (chosenFoodCategoryName.replace("FOOD CATEGORY", "").strip().capitalize()) in data:
                    print(data[2])
            input("\nPress Enter to Return")
            break
        except TypeError:
            print("Please enter a number")

'''New customer registration to access other details'''


'''DECLARING FUNCTIONS FOR REGISTERED CUSTOMER DASHBOARD'''
'''Login to access system'''
def readCustomerDetailsFile() -> list: #Reads file with customer details, extracts username and passwords without headers and appends it to list
    customerDetailsList = [] 
    try:
        with open (CUSTOMER_DETAILS_FILE,mode='r') as customerDetailsFile:
            skipFileLine(6,customerDetailsFile)
            for row in customerDetailsFile:
                customerDetailsList.append(row.strip("\n").replace(" | "," ").split(" "))
            return customerDetailsList
    except FileNotFoundError:
        print("Customers database is missing!")

def customerLoginPage():
    while True:
        clearConsole()
        pageBanners("Login as Customer", 50)
        try: 
            customerDetailsList = readCustomerDetailsFile()
            uName = userInput("Username",True)
            progressBar("Checking if username exists")
            time.sleep(0.05)
            if (authUsername(uName,customerDetailsList)):
                print(" Username found, please enter password\n")
                while True:
                    uPass = userInput("Password",True)
                    if (authPassword(uName, uPass,customerDetailsList)):
                        progressBar("Logging you in")
                        time.sleep(0.05)
                        break
                    else:
                        print("Incorrect password, please retry\n")
            else: 
                print(" Username not found, please retry")
                continue
            break
        except TypeError:
            print("Customers details file is corrupted!")
            break

def regCustomerMenu(): #Customer menu upon successful login
    while True:
        clearConsole()
        pageBanners("Customer Menu", 50)
        print("\nWelcome!, what would you like to do today?")
        print("1. View Item List", "2. View Item Details", "3. Add Food to Cart", "4. Checkout", "\n0. Main Menu", sep='\n')
        input = userInput("Choice",True)
        if input == "1":
            clearConsole()
            viewItemList()
        elif input =="2":
            viewItemDetail()
        elif input == "3":
            addFoodToCart()
        elif input =="4":
            checkout()
        elif input == "0":
            break
        else:pass
            # invalidInput()

'''View detail of food category'''
'''View detail of food items'''
'''Select food item and add to cart'''
'''Do payment to confirm order'''

'''DECLARING MAIN GREETING PAGE'''
def main(): #The main module that will be executed first
    while True:
        clearConsole()
        print(" ____   ___  _____ ____".center(78))
        print("/ ___| / _ \|  ___/ ___|".center(78))
        print("\___ \| | | | |_  \___ \\".center(78))
        print(" ___) | |_| |  _|  ___) |".center(80))
        print("|____/ \___/|_|   |____/".center(78))
        print("")
        print(f' {"Welcome to the Online Food Ordering Management System"} '.center(85, '='))
        time.sleep(1)
        print("\nWho are you logging in as?", "1. Admin", "2. Customer", "3. Quit Program", sep=' \n')
        try:
            input = int(userInput("Login as (1/2/3)",True))
            if input == 1 :
                clearConsole()
                pageBanners("ADMIN LOGIN PAGE",50)
                adminLoginPage()
            elif input == 2 :
                guestMenu() 
            elif input== 3 :
                quit()
            else:
                print("Out of range, please enter a number between 1 and 3")
                time.sleep(1)
                continue
            break
        except ValueError:
            print("You entered an alphabet, please enter a number between 1 and 3")
            time.sleep(1)
            

'''EXECUTE MAIN'''
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        quit()

# choices = [[1, "ADD NEW FOOD ITEM", addFoodItemMenu], [2, "MODIFY FOOD ITEM", modifyFoodItemMenu], [3, "DISPLAY RECORDS", displayRecordsMenu], [4, "SEARCH RECORDS", searchRecordsMenu]]
# userSelection = 2
# # pageBanner, functionCall = [choice[1], choice[2] for choice in choices if userSelection in choice]
# # print(userSelection in choices[(range(choices))]

# # for choice in choices:
# #     if userSelection == choice[0]:
# #         clearConsole()
# #         pageBanners(choice[1], 50)
# #         choice[2]()
# i=0
# print(i for i in range (len(choices)))

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
        # invalidInput()
        order()

def cancelOrder() : pass
def checkPayment() : pass
def viewItemList() : pass
def registered() : pass
def viewItemDetail() : pass
def viewCategoryDetail() : pass
def addFoodToCart() : pass
def checkout() : pass
def logout() : pass
def customerRegistration() : pass 