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
            if input == 1 :
                clearConsole()
                pageBanners("ADD NEW FOOD ITEM",50)
                addFoodItemMenu()
            elif input == 2 :
                clearConsole()
                pageBanners("MODIFY FOOD ITEM",50)
                modifyFoodItemMenu()
            elif input == 3 :
                displayRecordsMenu()
            elif input == 4 :
                searchRecordsMenu()
            elif input == 0 :
                progressBar("Logging out")
                main()
            else :
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

def displayFoodCategories(): #Displays list of food categories as ordered list
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

def updateFoodItemRecord(foodDetailsFile): #Updates record of food items in food details text file
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

def verifyFoodItemId(foodItemId,foodDetailsFile):
    if foodItemId == '' : 
        return False
    if (foodItemId[0].isalpha() and foodItemId[1 : len(foodItemId)].isdigit()):
        print(f"Food item id selected: {foodItemId}")
        for data in foodDetailsFile:
            if foodItemId in data[0]:
                return True

def listOutFoodItems(chosenFoodCategoryName):
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

def deleteFoodItemRecord(foodDetailsFile):
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
    rawList = []
    with open ('foodDetails.txt', mode='r') as foodDetailsFile:
        skipFileLine(2,foodDetailsFile)
        for line in foodDetailsFile:
            rawList.append(line.strip().replace('_','').split(","))
        for data in removeEmptyList(rawList):
            if (" | " in data[0]):
                index = rawList.index(data)
                rawList.pop(index)
    foodCategoryLists = [i for i in rawList if i != []]

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
def searchRecordsMenu():
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
                clearConsole()
                searchCustomerOrder()
            elif searchCategory == 2:
                clearConsole()
                searchCustomerPayment()
            else:
                print("The number you submitted is outside the allowed range!")
            break
        except ValueError:
            print("Please enter a number!")

'''Search Specific Customer Order Record'''
def searchCustomerOrder():
    print("_____________________".center(50))
    print("""
              CUSTOMER ORDER RECORD""")
    print("_____________________".center(50))
    print("""\n{}1. CUSTOMER USERNAME\t2. ORDER ID""".format(" "*4))
    print("\nOn what basis should the records be searched?".center(100))
    while True:
        try:
            orderList = readOrderRecordsFile()
            searchCriteria = int(userInput("Input 1 or 2",False))
            if (searchCriteria == 1):
                recordByUsername = []
                username = userInput("Please enter Customer Username",True)
                count = 0
                for data in orderList:
                    if (username.lower() == data[0]):
                        recordByUsername.append([data[1],data[2],data[3],data[7]])
                        count+=1
                if count >=1:
                    print("{} order records have been found for {}".format(count,username))
                    displayCustomerOrders(username)
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
                    displayCustomerOrders(orderID)
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

def displayCustomerOrders(criteria):
    progressBar("Generating report")
    time.sleep(0.5)
    print(
        """\n\t\t\t\tORDER REPORT FOR {}
\t\t\t\t-----------------{}\n""".format(
            criteria.upper(), "-" * len(criteria)
        )
    )

    print("""CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)
-----------------       --------        -------------   ------------    -----------------""")

'''Search Specific Customer Payment Record'''
def searchCustomerPayment():
    print("_______________________".center(50))
    print("""
             CUSTOMER PAYMENT RECORD""")
    print("_______________________".center(50))
    print("""\n{}1. CUSTOMER USERNAME\t2. ORDER ID""".format(" "*4))
    print("\nOn what basis should the records be searched?".center(100))
    while True:
        try:
            paymentList = readOrderRecordsFile()
            searchCriteria = int(userInput("Input 1 or 2",False))
            if (searchCriteria == 1):
                recordByUsername = []
                username = userInput("Please enter Customer Username",True)
                count = 0
                for data in paymentList:
                    if (username.lower() == data[0]):
                        recordByUsername.append([data[1],data[3],data[4],data[5],data[6]])
                        count+=1
                if count >=1:
                    print("{} order records have been found for {}".format(count,username))
                    displayCustomerPayments(username)
                    for data in recordByUsername:
                        print('{:<24}{:<16}{:<16}{:<16}{:<17}{}'.format(username.upper(),data[0],data[1],data[2],data[3],data[4]))
                else:
                    print("No order records found for {}".format(username))
                break
            if (searchCriteria == 2):
                orderID = userInput("Please enter Order ID",True)
                recordById = []
                orderExists = False
                for data in paymentList:
                    if (orderID.upper() == data[1]):
                        recordById.append([data[0],data[1],data[3],data[4],data[5],data[6]])
                        orderExists = True
                if (orderExists):
                    print("1 Order record have been found for Order ID {}".format(orderID.upper()))
                    displayCustomerPayments(orderID)
                    for data in recordById:
                        print('{:<24}{:<16}{:<16}{:<16}{:<17}{}'.format(data[0].upper(),data[1],data[2],data[3],data[4],data[5]))
                else:
                    print("No order records found for {}".format(orderID.upper()))
                break
            else:
                print("The number you submitted is outside the allowed range!")
                time.sleep(1)
        except ValueError:
            print("Please submit a number")
            time.sleep(1)

def displayCustomerPayments(criteria):
    progressBar("Generating report")
    time.sleep(0.5)
    print(
        """\n\t\t\t\t\tPAYMENT REPORT FOR {}
\t\t\t\t\t-------------------{}\n""".format(
            criteria.upper(), "-" * len(criteria)
        )
    )

    print("""CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\t PAID ON
-----------------       --------        -------------   --------------  --------------   -------""")

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
    print(" ____   ___  _____ ____".center(78))
    print("/ ___| / _ \|  ___/ ___|".center(78))
    print("\___ \| | | | |_  \___ \\".center(78))
    print(" ___) | |_| |  _|  ___) |".center(80))
    print("|____/ \___/|_|   |____/".center(78))
    print("")
    print(f' {"Welcome to the Online Food Ordering Management System"} '.center(85, '='))
    time.sleep(1)
    print("\nWho are you logging in as?", "1. Admin", "2. Customer", "3. Quit Program", sep=' \n')
    while (True):
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
                continue
            break
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
def viewCategoryList() : pass
def viewItemList() : pass
def registered() : pass
def viewItemDetail() : pass
def viewCategoryDetail() : pass
def addFoodToCart() : pass
def checkout() : pass
def logout() : pass
def customerRegistration() : pass 
