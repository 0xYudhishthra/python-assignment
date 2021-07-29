#Yudhishthra A/L S Sugumaran - TP061762
#Choong Wei Jun - TP061867

"""
Code Structure
1. Import necessary external modules
2. Declaring functions to read text files and convert it to lists
3. Declaring functions that can be used in any part of the program
4. Declaring functions for admin dashboard
    0. Login to Access System (Done)
    1. Add food item by category (Done)
    2. Modify food item (Update, Delete) (Done)
    3. Display Records of Food Category (Done)
    4. Display Records of Food Items by Category (Done)
    5. Display Records of Customer Orders (Done)
    6. Display Records of Customer Payments (Done)
    7. Search Specific Customer Order Record (Done)
    8. Search Specific Customer Payment Record (Done)
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

'''DECLARING FUNCTIONS TO CONVERT TEXT FILES TO LISTS'''
def readAdminDetailsFile(): #Reads file with admin details, extracts username and passwords without headers and appends it to list
    adminDetailsList = [] 
    while (True):
        try:
            with open ('adminDetails.txt',mode='r') as adminDetailsFile:
                skipFileLine(6,adminDetailsFile)
                for row in adminDetailsFile:
                    adminDetailsList.append(row.strip("\n").replace(" | "," ").split(" "))
                return adminDetailsList
        except FileNotFoundError:
            print("Admin database is missing!") 
        break

def readFoodDetailsFile(): #Reads file with food details, extract food details without headers and appends it to list 
    foodDetailsList=[]
    while True:
        try:
            with open ('foodDetails.txt', mode='r') as foodDetailsFile:
                skipFileLine(6,foodDetailsFile) 
                for row in foodDetailsFile:
                    if row.startswith("_"):
                        skipFileLine(3,foodDetailsFile)
                    foodDetailsList.append(row.replace("\n","").replace("_","").split(" | "))
                return removeEmptyList(foodDetailsList)
        except FileNotFoundError:
            print("Food details database is missing!") 
        break

def readOrderRecordsFile(): #Reads file with order records, extract order records without headers and append to list
    while True:
        try:
            with open('orderRecords.txt', mode='r') as orderRecordsFile:
                skipFileLine(6,orderRecordsFile)
                orderDetailsList = [line.strip('\n').split(" | ") for line in orderRecordsFile]
            return orderDetailsList
        except FileNotFoundError:
            print("Order records database is missing!")
        break

def readCustomerDetailsFile(): #Reads file with customer details, extracts username and passwords without headers and appends it to list
    customerDetailsList = [] 
    while (True):
        try:
            with open ('customerDetails.txt',mode='r') as customerDetailsFile:
                skipFileLine(6,customerDetailsFile)
                for row in customerDetailsFile:
                    customerDetailsList.append(row.strip("\n").replace(" | "," ").split(" "))
                return customerDetailsList
        except FileNotFoundError:
            print("Customers database is missing!") 
        break


'''DECLARING FUNCTIONS THAT CAN BE USED ANYWHERE IN THE PROGRAM'''
def clearConsole(): #Function to clear all existing text in console
    if os.name in ('nt', 'dos'):  
        os.system('cls')
    else:
        os.system("clear")

def quit() : #Exits program cleanly
    clearConsole()
    print("Exiting...")
    time.sleep(2)
    clearConsole()
    exit()

def userInput(inputString, skipLine): #Function to accept input from users
    if (skipLine):
        return input("\n{} >> ".format(inputString))
    else:
        return input("{} >> ".format(inputString))

def authUsername(username,filename):  #Checks if username exists in the respective filename given
        for data in filename:
            if username == data[0]:
                return True

def authPassword(username, password,filename):  #Checks if password exists in the respective filename given
    for data in filename:
        if username == data[0] and password == data[1]:
            return True

def skipFileLine(count,filename): #Skips n number of lines in a file that is being read/write 
        for _ in range(count):
            next(filename)

def removeEmptyList(list): #Removes list with empty strings and lists with no elements
    for data in list:
        while ('' in data):
            data.remove('')
        new_list = [i for i in list if i != []]
    return new_list

def progressBar(loadingMessage): #Loading animation
    print('{}...'.format(loadingMessage))
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for item in animation:
        time.sleep(0.05)
        print("\r" + item, end="")

def pageBanners(pageTitle,centerLength): #Main page banner
    print(f'{"_"*(len(pageTitle))}\n'.center(centerLength))
    print(f'{pageTitle}'.center(centerLength))
    print(f'{"_"*len(pageTitle)}'.center(centerLength))

'''DECLARING FUNCTIONS FOR ADMIN DASHBOARD'''
'''Login to access system'''
def adminLoginPage(): #Login Page for SOFS adminstrators
    while True:
        try: 
            uName = userInput("Username",True)
            progressBar("Checking if username exists")
            time.sleep(0.05)
            if (authUsername(uName,readAdminDetailsFile())):
                print(" Username found, please enter password\n")
                while True:
                    uPass = userInput("Password",True)
                    if (authPassword(uName, uPass,readAdminDetailsFile())):
                        progressBar("Logging you in")
                        time.sleep(0.05)
                        adminMenu(uName)
                        break
                    else:
                        print("Incorrect password, please retry\n")
            else: 
                print(" Username not found, please retry")
                continue
            break
        except TypeError:
            print("Admin details file is corrupted!")
            break

def adminMenu(uName=""): #Admin Menu shown upon successful login
    while True:
        try:
            clearConsole()
            pageBanners("ADMIN DASHBOARD",50)
            print(f'\nHey, {uName.capitalize()}! What would you like to do today?\n')
            print("1. Add food item","2. Modify food item","3. Display records","4. Search record","0. Log out", sep='\n')
            input = int(userInput("I would like to",True))
            if input == 0:
                progressBar("Logging out")
                main()
            elif input == 1:
                clearConsole()
                pageBanners("ADD NEW FOOD ITEM",50)
                addFoodItemMenu()
            elif input == 2:
                clearConsole()
                pageBanners("MODIFY FOOD ITEM",50)
                modifyFoodItemMenu()
            elif input == 3:
                clearConsole()
                pageBanners("DISPLAY RECORDS",50)
                displayRecordsMenu()
            elif input == 4:
                clearConsole()
                pageBanners("SEARCH RECORDS",50)
                searchRecordsMenu()
            else:
                print("Number is out of range!")
                time.sleep(1)
                continue
            break
        except ValueError:
            print("Please submit a number")
            time.sleep(1) 

'''Add food item by category'''
def addFoodItemMenu(): #Prompts admin to select which category of food item they want to add or to add new food category 
    while True:
        try:
            print(f"\nIn which category would you like to add the food item?\n\n0. Add new food category")
            displayFoodCategories()
            chosenFoodCategoryNumber = int(userInput("Food Category Number",True))
            if (chosenFoodCategoryNumber == 0): 
                writeNewFoodCategoryToFile(userInput("Category Name",False),userInput("Description",False))
            elif (chosenFoodCategoryNumber > 0 and chosenFoodCategoryNumber <= len(extractFoodCategories())): 
                chosenFoodCategoryName = extractFoodCategories()[int(chosenFoodCategoryNumber)-1][0].replace("FOOD CATEGORY","").strip().capitalize()
                foodItemName = userInput("New Food Item Name",False)
                foodItemPrice = format(float(userInput("New Food Item Price",False)),".2f")
                print(f"\nFOOD CATEGORY\tFOOD ITEM PRICE\t FOOD ITEM NAME\n{'-'*13}{' '*3}{'-'*15}{' '*2}{'-'*14}")
                print('{:<16}{:<17}{}'.format(chosenFoodCategoryName,foodItemPrice,foodItemName))
                print("\nPlease confirm the new food details you would like to add")
                userConfirmation = userInput("(Y)es/(N)o",False)
                if (userConfirmation.upper() == 'Y'):
                    writeNewFoodItemToFile(chosenFoodCategoryName,foodItemName,foodItemPrice)
                elif (userConfirmation.upper() == 'N'):
                    addFoodItemMenu()
                else:
                    print("Please enter either Y or N")
                    continue
                break
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

def writeNewFoodCategoryToFile(categoryName,categoryDescription): #Adds new food category in food details file
    uppercaseName = categoryName.upper()
    capitalizedDescription = categoryDescription.capitalize()
    with open('foodDetails.txt','a') as foodDetailsFile:
            foodDetailsFile.write('\n' + '_'*88 + '\n\n')
            foodDetailsFile.write(f"{uppercaseName} FOOD CATEGORY - {capitalizedDescription}\n")
            foodDetailsFile.write("_"*88 + '\n')

def writeNewFoodItemToFile(foodCategoryName,foodItemName,foodItemPrice): #Directly writes new food item data to food details file
    try:
        orderRecordsFile = []
        with open ('foodDetails.txt', mode='r') as f:
            for row in f:   
                orderRecordsFile.append([row])
        foodItemIndexes = [
            orderRecordsFile.index(data)
            for data in orderRecordsFile
            if foodCategoryName in data[0]
        ]
        lastFoodItemIndex = foodItemIndexes[-1]
        lastFoodItemRecord = orderRecordsFile[lastFoodItemIndex][0].split(" | ")
        newFoodID = lastFoodItemRecord[0][0] + str(int(lastFoodItemRecord[1].strip(lastFoodItemRecord[0][0]))+1)
        if (lastFoodItemIndex == (len(orderRecordsFile)-1)):
            orderRecordsFile.insert(lastFoodItemIndex+1, [f'\n{foodCategoryName} | {newFoodID} | {foodItemName} | {foodItemPrice}'])
        else:
            orderRecordsFile.insert(lastFoodItemIndex+1, [f'{foodCategoryName} | {newFoodID} | {foodItemName} | {foodItemPrice}\n'])
        with open ('foodDetails.txt', mode='w') as food:
            for data in orderRecordsFile:       
                food.write(data[0])
    except TypeError:
        print("Food details text file is corrupted!")
    except FileNotFoundError:
        print("Food details text file is missing!")

def displayFoodCategories(): #Displays list of food categories ONLY as ordered list
    while True:
        try:     
            count=1
            while (count<len(extractFoodCategories())):
                for list in extractFoodCategories():
                    print(f'{count}. {list[0].capitalize()}')
                    count+=1
            break
        except TypeError:
            print("Food details file is corrupted!")
            break

def extractFoodCategories(): #Gets the title and description of the food categories from the food details text file and append it to list
    while True:
        try:
            rawList = []
            foodCategoryDetails = []
            with open ('foodDetails.txt', mode='r') as foodDetailsFile:
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
        break

'''Modify food item'''
def modifyFoodItemMenu(): #Main page for admins to modify records of food items
    foodDetailsFile = []
    with open('foodDetails.txt',mode='r') as foodFile:
        for row in foodFile:
            foodDetailsFile.append([row])
    print("\n{}1. UPDATE RECORD\t2. DELETE RECORD".format(" "*5))
    print("\nWhat would you like to do?")
    while (True):
        try:
            modifyChoice = int(userInput("Input 1 or 2",False))
            if modifyChoice == 1:
                clearConsole()
                pageBanners("UPDATE FOOD ITEM",50)
                updateFoodItemRecord(foodDetailsFile)
            elif modifyChoice == 2:
                clearConsole()
                pageBanners("DELETE FOOD ITEM",50)
                deleteFoodItemRecord(foodDetailsFile)
            else:
                print("Number is out of range")
                continue
            break
        except ValueError:
            print("Please submit a number")
            continue

def updateFoodItemRecord(foodDetailsFile): #Updates a specific record of food item in the food details text file
    # sourcery no-metrics
    while True:
        try:
            print("\nIn which category would you like to update the food item?")
            displayFoodCategories()
            categoryNumber = int(userInput("Category number",True))
            if 0 < categoryNumber <= len(extractFoodCategories()):
                listOutFoodItems(extractFoodCategories()[categoryNumber-1][0])  
            else:
                print("Number is out of range")
                continue
            foodItemId = userInput("Enter the Food Item ID that you would like to update",True).upper()
            if (verifyFoodItemId(foodItemId,foodDetailsFile)):
                for data in foodDetailsFile:
                    if foodItemId in data[0]:
                        foodItemIdList = (data[0].split(" | "))
                        foodItemIdIndex = foodDetailsFile.index(data)
                    if foodItemId not in data[0]:
                        print("Invalid Food Item ID")
                        break
                    continue
                print("\nWhat would you like to update?","1. Food Item Price","2. Food Item Name","3. Both",sep='\n')
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
            else:
                print("Invalid food item id")
                continue
            foodDetailsFile[foodItemIdIndex] = [" | ".join(foodItemIdList)]
            with open ('foodDetails.txt',mode='w') as f:
                f.write(data[0] for data in foodDetailsFile)
            break
        except FileNotFoundError:
            print("Food details file not found")
            break
        except ValueError:
            print("Please submit a number")
            continue

def verifyFoodItemId(foodItemId,foodDetailsFile): #Verifies the format of the food item ID that has been received by the user
    if foodItemId == '' : 
        return False
    if (foodItemId[0].isalpha() and foodItemId[1 : len(foodItemId)].isdigit()):
        print(f"Food item id selected: {foodItemId}")
        for data in foodDetailsFile:
            if foodItemId in data[0]:
                return True

def listOutFoodItems(chosenFoodCategoryName): #Displays the details of all food items in the food details file based on the category chosen by the user
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

def deleteFoodItemRecord(foodDetailsFile): #Deletes a specific food item record in the food details text file
    while True:
        try:
            print("\nIn which category would you like to delete the food item?")
            displayFoodCategories()
            categoryNumber = int(userInput("Category number",True))
            if 0 < categoryNumber <= len(extractFoodCategories()):
                listOutFoodItems(extractFoodCategories()[categoryNumber-1][0])  
            else:
                print("Number is out of range")
                continue
            foodItemId = userInput("Enter the Food Item ID that you would like to delete",True).upper()
            if(verifyFoodItemId(foodItemId,foodDetailsFile)):
                print(f"Are you sure you want to delete {foodItemId}?")
                userConfirmation = userInput("(Y)es/(N)o",True).upper()
                if (userConfirmation=="Y"):
                    for data in foodDetailsFile:
                        if foodItemId in data[0]:
                            foodDetailsFile.pop(foodDetailsFile.index(data))
                        if '\n' in foodDetailsFile[-1][-1]:
                            temp = foodDetailsFile[-1][-1].strip("\n")
                            foodDetailsFile[-1][-1] = temp
                    with open ('foodDetails.txt',mode='w') as f:
                        for data in foodDetailsFile:
                            f.write(data[0])
                    break
                elif (userConfirmation == "N"):
                    adminMenu()
                else:
                    print("Invalid input")
            else:
                print("Invalid Food Item ID")
                continue
        except ValueError:
            print("Please submit a number")
            time.sleep(1)

'''Main Menu Page for Display'''
def displayRecordsMenu(): #Display records main page
    print("\n1. Food Categories","2. Food Items by Category","3. Customer Orders","4. Customer Payment","0. Back to Admin  Menu", sep='\n')  
    while True:
        try:
            orderRecordsList = readOrderRecordsFile()
            foodCategoryList = extractFoodCategories()
            input = userInput("Display all records of",True)
            if input == "1" :
                progressBar("Generating report")
                displayFoodCategoryRecords(foodCategoryList)
            elif input == "2" :
                print("\nSelect the food category that you want to be displayed")
                displayFoodCategories()
                chosenCategory = int(userInput("Food category",True))
                listOutFoodItems((extractFoodCategories()[chosenCategory-1][0]))
            elif input == "3" :
                progressBar("Generating report")
                displayOrderOrPaymentRecords('orders',orderRecordsList)
            elif input == "4" :
                progressBar("Generating report")
                displayOrderOrPaymentRecords('payments',orderRecordsList)
            elif input == "0" :
                adminMenu()
            else :
                print("Number out of range")
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
def searchRecordsMenu(): #Main page to search records
    print("\n1. CUSTOMER ORDER RECORD\t2. CUSTOMER PAYMENT RECORD".center(50))
    print("\nWhich record do you want to check?")
    while (True):
        try:
            orderRecordsList = readOrderRecordsFile()
            searchCategory = int(userInput("Input 1 or 2",False))
            if searchCategory == 1:
                clearConsole()
                pageBanners("SEARCH CUSTOMER ORDER",50)
                searchCustomerOrder(orderRecordsList)
            elif searchCategory == 2:
                clearConsole()
                pageBanners("SEARCH CUSTOMER PAYMENT",50)
                searchCustomerPayment(orderRecordsList)
            else:
                print("The number you submitted is outside the allowed range!")
            break
        except ValueError:
            print("Please enter a number!")

'''Search Specific Customer Order Record'''
def searchCustomerOrder(orderRecordsList): #Searches the order records file for a specific customer order record
    print("""\n{}1. CUSTOMER USERNAME\t2. ORDER ID""".format(" "*4))
    print("\nOn what basis should the records be searched?".center(100))
    while True:
        try:
            searchCriteria = int(userInput("Input 1 or 2",False))
            if (searchCriteria == 1):
                recordByUsername = []
                username = userInput("Please enter Customer Username",True)
                count = 0
                for data in orderRecordsList:
                    if (username.lower() == data[0]):
                        recordByUsername.append([data[0],data[1],data[2],data[3],data[7]])
                        count+=1
                if count >=1:
                    print("{} order records have been found for {}".format(count,username))
                    displaySearchResults('orders',username,recordByUsername)
                else:
                    print("No order records found for {}".format(username))
                    continue
            elif (searchCriteria == 2):
                orderID = userInput("Please enter Order ID",True)
                recordById = []
                orderExists = False
                for data in orderRecordsList:
                    if (orderID.upper() == data[1]):
                        recordById.append([data[0],data[1],data[2],data[3],data[7]])
                        orderExists = True
                if (orderExists):
                    print("1 Order record have been found for Order ID {}".format(orderID.upper()))
                    displaySearchResults('orders',orderID,recordById)
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

'''Search Specific Customer Payment Record'''
def searchCustomerPayment(paymentList): #Searches the order records file for a specific customer payment record
    print("""\n{}1. CUSTOMER USERNAME\t2. ORDER ID""".format(" "*4))
    print("\nOn what basis should the records be searched?".center(100))
    while True:
        try:
            searchCriteria = int(userInput("Input 1 or 2",False))
            if (searchCriteria == 1):
                recordByUsername = []
                username = userInput("Please enter Customer Username",True)
                count = 0
                for data in paymentList:
                    if (username.lower() == data[0]):
                        recordByUsername.append([data[0],data[1],data[3],data[4],data[5],data[6]])
                        count+=1
                if count >=1:
                    print("{} order records have been found for {}".format(count,username))
                    displaySearchResults('payments',username,recordByUsername)
                else:
                    print("No order records found for {}".format(username))
                break
            if (searchCriteria == 2):
                orderID = userInput("Please enter Order ID",True)
                recordById = []
                orderIdExists = False
                for data in paymentList:
                    if (orderID.upper() == data[1]):
                        recordById.append([data[0],data[1],data[3],data[4],data[5],data[6]])
                        orderIdExists = True
                if (orderIdExists):
                    print("1 Order record have been found for Order ID {}".format(orderID.upper()))
                    displaySearchResults('payments',orderID,recordById)
                else:
                    print("No order records found for {}".format(orderID.upper()))
                break
            else:
                print("The number you submitted is outside the allowed range!")
                time.sleep(1)
        except ValueError:
            print("Please submit a number")
            time.sleep(1)

'''Display Search Results'''
def displaySearchResults(recordName,searchBasis,resultsList): #Gets search results from the earlier search functions and displays it cleanly
    while True:
        progressBar("Generating report")
        time.sleep(0.5)
        if recordName == 'orders':
            print(f"\n\t\t\t\tORDER REPORT FOR {searchBasis.upper()}\n{'-' * len(searchBasis)}\t\t\t\t{'-'*17}\n")
            print(f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*12}{' '*4}{'-'*17}")
            for data in resultsList:
                print('{:<24}{:<16}{:<16}{:<16}{}'.format(data[0].upper(),data[1],data[3],data[4],data[2]))           
        else:
            print(f"\n\t\t\t\tPAYMENT REPORT FOR {searchBasis.upper()}\n\t\t\t\t{'-'*19}{'-' * len(searchBasis)}\n")
            print(f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\tPAID ON\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*14}{' '*2}{'-'*14}{' '*2}{'-'*7}")
            for data in resultsList:
                print('{:<24}{:<16}{:<16}{:<16}{:<16}{}'.format(data[0].upper(),data[1],data[2],data[3],data[4],data[5]))  
        break

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
            invalidInput()
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
def customerLoginPage():
    while True:
        clearConsole()
        pageBanners("Login as Customer", 50)
        try: 
            uName = userInput("Username",True)
            progressBar("Checking if username exists")
            time.sleep(0.05)
            if (authUsername(uName,readCustomerDetailsFile())):
                print(" Username found, please enter password\n")
                while True:
                    uPass = userInput("Password",True)
                    if (authPassword(uName, uPass,readCustomerDetailsFile())):
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
        else:
            invalidInput()

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
        except ValueError:
            print("You entered an alphabet, please enter a number between 1 and 3")
            

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
def viewItemList() : pass
def registered() : pass
def viewItemDetail() : pass
def viewCategoryDetail() : pass
def addFoodToCart() : pass
def checkout() : pass
def logout() : pass
def customerRegistration() : pass 