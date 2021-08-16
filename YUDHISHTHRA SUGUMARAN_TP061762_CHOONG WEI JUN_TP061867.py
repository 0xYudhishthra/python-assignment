# Yudhishthra A/L S Sugumaran - TP061762
# Choong Wei Jun - TP061867

#!/usr/bin/env python3

'''IMPORT NECESSARY EXTERNAL MODULES'''
import os
import time

'''UTILITY FUNCTIONS'''
def initialProgramCheck(): #Function that ensures all files needed exists and has data, update pseudocode
    print(" PRE-PROGRAM CHECKS ".center(85,"="))
    print(" File Existence Check ".center(85,'='))
    files = ["./foodDetails.txt", "./customerDetails.txt", "./adminDetails.txt", "./orderRecords.txt"]
    #Iterates thorugh each file in the files list to see if it exists in the given directory
    for file in files:
        print(f"Checking if {file} exists", end="") 
        time.sleep(0.5)
        if os.path.exists(file):
            print (f" -> {file} exists")
        else:
            print(f" -> {file} not found")
            print("ERROR: Program failed to execute")
            exit()
    print(" Data Existence Check ".center(85,'='))
    #Reads in each file in the files list, append to contentList and checks if list is empty or not
    for file in files:
        contentList = []
        print(f"Checking for data presence in {file}",end="")
        time.sleep(0.5)
        with open(file,mode='r') as dataFile:
            skipFileLine(6, dataFile)
            for line in dataFile:
                contentList.append(line)
        if contentList == []:
            print(f" -> No data in {file}")
            print("ERROR: Program failed to execute")
            exit()
        else:
            print(f" -> Data exists in {file}")

def clearConsole(): #Function to clear all existing text in console
    #Submits console "clear" command depending on os type
    os.system("cls") if (os.name in ("nt", "dos")) else os.system("clear")

def quit() : #Function to exit program cleanly
    print("\n")
    print(f' {"Thank you! Please come again"} '.center(85, '='))   
    time.sleep(0.5)
    exit()

def userInput(promptMessage:str, skipLine:bool) -> input: #Function to format prompt message to accept input from users 
    #Asks for input after optionally skipping a line based on the skipLine value
    if (skipLine):
        return input(f"\n{promptMessage} >> ")
    else:   
        return input(f"{promptMessage} >> ")

def authUsername(username:str, detailsList:list) -> bool:  #Function that verifies if username exists in the respective list 
    #detailsList can either be adminDetails or customerDetails, data[0] because that sublist contains the usernames
    for data in detailsList:
        if username == data[0]:
            return True

def authPassword(username:str, password:str, detailsList:list) -> bool:  #Function that verifies if password exists in the respective list
    #detailsList can either be adminDetails or customerDetails, data[0] and data[1] is used to check if the password is the one that matches the username
    for data in detailsList:
        if username == data[0] and password == data[1]:
            return True

def skipFileLine(count:int,fileHandle): #Function that skips n number of lines in a file handle (textIOWrapper) that is being read/write 
    for _ in range(count):
        next(fileHandle) 
            
def removeEmptyList(sourceList:list) -> list: #Function that removes list with empty strings and lists with no elements
    for data in sourceList:
        while ('' in data):
            data.remove('')
    return [data for data in sourceList if data != []]

def progressBar(loadingMessage:str): #Function that displays loading animation with message
    print(f'{loadingMessage}...')
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                 "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for item in animation:
        time.sleep(0.05)
        #carriage return to return cursor to start after displaying 1 item in animation thus displaying a "loading" kind of output
        print("\r" + item, end="")

def pageBanners(pageTitle:str,centerLength:int): #Function that displays banner for each different pages for respective dashboards
    print(f'\t{"_"*(len(pageTitle))}\n'.center(centerLength))
    print(f'\t{pageTitle} '.center(centerLength))
    print(f'\t{"_"*len(pageTitle)} '.center(centerLength))


'''DECLARING FUNCTIONS FOR ADMIN DASHBOARD'''
'''Login to access system'''
def readAdminDetailsFile() -> list: #Function that reads file with admin details, extracts username and passwords without headers and appends it to list, PSEUDOCODE TBC
    adminDetailsList = [] 
    with open ("./adminDetails.txt",mode='r') as adminDetailsFile:
        skipFileLine(6,adminDetailsFile)
        for row in adminDetailsFile:
            #Remoes unnecessary foreign elements to only append usernames and password to list
            adminDetailsList.append(row.strip("\n").replace(" | "," ").split(" ")) 
    return adminDetailsList

def adminLoginPage(): #Function that displays login Page for SOFS adminstrators, TO-DO: show message when user enter without submitting anything
    adminDetailsList = readAdminDetailsFile()
    usernameExists = False
    uName = ''
    #Continuosly ask for username until it user input matches any 1 usernames in the adminDetailsList
    while(not usernameExists):
        uName = userInput("Username",True).lower()
        if uName == "" : 
            print("ERROR: Username not submitted")
            continue
        progressBar("Authenticating username")
        time.sleep(0.05)
        usernameExists = authUsername(uName,adminDetailsList)
        print(" Username found, please enter password\n") if (usernameExists) else print(" ERROR: Username not found\n")
    #Continuously asks for password until it matches the username given earlier
    while (usernameExists):
        uPass = userInput("Password",True)
        if uPass == "" : 
            print("ERROR: Password not submitted")
            continue
        progressBar("Authenticating password")
        time.sleep(0.05)
        passwordMatch = authPassword(uName, uPass,adminDetailsList)
        if (passwordMatch):
            adminMenu(uName)
            break  
        else: 
          print(" ERROR: Incorrect password")

def adminMenu(uName:str = 'Admin'): #Function that shows admin Menu upon successful admin login, PSEUDOCODE TO BE CHANGED
    CHOICES = [[1, "ADD NEW FOOD ITEM", addFoodItemMenu], [2, "MODIFY FOOD ITEM", modifyFoodItemMenu], 
               [3, "DISPLAY RECORDS", displayRecordsMenu], [4, "SEARCH RECORDS", searchRecordsMenu]]
    clearConsole()
    pageBanners("ADMIN DASHBOARD",50)
    print(f'\nWhat would you like to do today?\n')
    print("1. Add food item","2. Modify food item","3. Display records","4. Search record","\n0. Log out", sep='\n')
    #Redirects user based on chosen option and also to prevent invalid inputs
    while True:
        try:
            userSelection = int(userInput("I would like to (Number)",True))
            if userSelection == 0:
                progressBar("Logging out")
                main()
            elif userSelection > len(CHOICES) or userSelection < 0:
                print("ERROR: Number is out of range")
                time.sleep(0.1)
                continue
            for choice in CHOICES:
                if userSelection == choice[0]:
                    clearConsole()
                    pageBanners(choice[1],50)
                    choice[2]()
            break
        except ValueError:
            print("ERROR: Foreign character submitted")
            time.sleep(0.1) 

'''Add food item by category'''
def readFoodDetailsFile() -> list: #Function that reads file with food details, extract food details without headers and appends it to list, TO-DO: modify try-catch to fit missing files
    foodItemsList=[]
    with open ("./foodDetails.txt", mode='r') as foodDetailsFile:
        skipFileLine(6,foodDetailsFile) 
        for row in foodDetailsFile:
            if row[0] == "_": #Skips food category name and description
                skipFileLine(3,foodDetailsFile)
            foodItemsList.append(row.replace("\n","").replace("_","").split(" | "))
    return removeEmptyList(foodItemsList)

def displayFoodCategories(): #Function that displays list of food categories ONLY as ordered list, update pseudocode, rethink purpose of this function
    foodCategoriesList = extractFoodCategoryTitles()
    for list in foodCategoriesList:
        print(f'{foodCategoriesList.index(list)+1}. {list[0].capitalize()}')
        
def addFoodItemMenu(): #Function that prompts admin to select which category of food item they want to add or to add new food category, PSEUDOCODE TO BE CHANGED, to update
    foodCategoryTitles = extractFoodCategoryTitles()
    print(f"\nIn which category would you like to add the food item?\n")
    displayFoodCategories()
    print(f"\n{len(foodCategoryTitles)+1}. Add new food category")
    print(f"0. Back to Admin Menu")
    #Redirects user based on chosen option
    while True:
        try:
            chosenFoodCategoryNumber = int(userInput("Food Category Number",True))
            if (chosenFoodCategoryNumber == len(foodCategoryTitles)+1): 
                writeNewFoodCategoryToFile()
                time.sleep(0.5)
                adminMenu()
            elif ( 0 < chosenFoodCategoryNumber <= len(foodCategoryTitles)): 
                chosenFoodCategoryName = foodCategoryTitles[int(chosenFoodCategoryNumber)-1][0].replace("FOOD CATEGORY","").strip().capitalize()
                getNewFoodItemDetails(chosenFoodCategoryName)  
                time.sleep(0.5)
                adminMenu()
            elif chosenFoodCategoryNumber == 0:
                adminMenu()
            else:
                print("ERROR: Food category number out of range")
                time.sleep(0.1)
                continue
            break
        except ValueError:
            print("ERROR: Foreign character submitted")
            time.sleep(0.1)
        

def getNewFoodItemDetails(chosenFoodCategoryName:str) -> str: #Function that gets details of new food item from user before being written to file , to update
    validFoodItemName = False
    validFoodItemPrice = False
    #Ensures the foodItemName is in a valid format
    while (not validFoodItemName):
        foodItemName = userInput("\nNew Food Item Name",False)
        if foodItemName == "" or foodItemName.isdigit(): 
            print("Invalid food item name!")
            continue
        elif (len(foodItemName) < 5):
            print("Food item name cannot be less than 5 characters!")
            continue
        else:
            validFoodItemName = True
    #Ensures the foodItemPrice is in a valid format
    while(not validFoodItemPrice):
        try:
            foodItemPrice = float(userInput("\nNew Food Item Price",False))
            if foodItemPrice == 0.0 or foodItemPrice < 0.0:
                print("Invalid food item price!")
                continue
            else:
                validFoodItemPrice = True
                foodItemPrice = format(foodItemPrice, ".2f")
        except ValueError:
            print("Please enter a valid food item price")
    #Confirms new addition to the food details file
    print(f"\nFOOD CATEGORY\tFOOD ITEM PRICE\t FOOD ITEM NAME\n{'-'*13}{' '*3}{'-'*15}{' '*2}{'-'*14}")
    print('{:<16}{:<17}{}'.format(chosenFoodCategoryName,foodItemPrice,foodItemName))
    print("\nPlease confirm the new food details you would like to add")
    while True:
        userConfirmation = userInput("(Y)es/(N)o",False).upper()
        if (userConfirmation == 'Y'):
            progressBar("Writing to file")
            time.sleep(0.5)
            writeNewFoodItemToFile(chosenFoodCategoryName,foodItemName,foodItemPrice)
        elif (userConfirmation == 'N'):
            addFoodItemMenu()
        else:
            print("\nERROR: Please enter either Y or N")
            continue
        break
            
        
def writeNewFoodCategoryToFile(): #Function that adds new food category in food details file and asks user if they want to add a new food item in the new category, update pseudocode
    #Add new food category to file
    addFoodCategoryConfirmation = False
    foodCategoryName = userInput("\nNew Food Category Name",False).upper()
    foodCategoryDescription = userInput("\nNew Food Category Description",False).capitalize()
    print(f"\nFOOD CATEGORY NAME\tFOOD CATEGORY DESCRIPTION\n{'-'*18}\t{'-'*25}")
    print('{:<16}\t{:<17}'.format(foodCategoryName,foodCategoryDescription))
    print("\nPlease confirm the new food category you would like to add")
    while not addFoodCategoryConfirmation:
        userConfirmation = userInput("(Y)es/(N)o",False).upper()
        if (userConfirmation == 'Y'):
            progressBar("Adding new food category")
            time.sleep(0.5)
            with open("./foodDetails.txt",'a') as foodDetailsFile:
                foodDetailsFile.write('\n' + '_'*88 + '\n\n')
                foodDetailsFile.write(f"{foodCategoryName} FOOD CATEGORY - {foodCategoryDescription}\n")
                foodDetailsFile.write("_"*88)
                addFoodCategoryConfirmation = True
            print(" Success!")
        elif (userConfirmation == 'N'):
            addFoodItemMenu()
        else:
            print("\nERROR: Please enter either Y or N")
            continue
        break
    while addFoodCategoryConfirmation:    
    #Option to add food item in new category
        print(f"\nWould you like to add a new food item in this category?")
        userConfirmation = userInput("(Y)es/(N)o",False).upper()
        if userConfirmation == 'Y':
            getNewFoodItemDetails(foodCategoryName.capitalize())
        elif userConfirmation == 'N':
            addFoodItemMenu()
        else:
            print("ERROR: Please enter either Y or N")
            continue
        break

def writeNewFoodItemToFile(foodCategoryName:str,foodItemName:str,foodItemPrice:float): #Function that directly writes new food item data to food details file
    foodItemsList = []
    #Appends every line from the file to foodItemsList
    with open ("./foodDetails.txt", mode='r') as f:
        for row in f:   
            foodItemsList.append([row])
    #Gets indexes of food item that have the same category name that is being searched and append it to foodItemIndexes using list comprehension
    foodItemIndexes = [
        foodItemsList.index(data)
        for data in foodItemsList
        if foodCategoryName.capitalize() == data[0][0:len(foodCategoryName)]
    ]
    #Assigns a default ID by combining first letter of the food category name and the number 1 for food category that does not have any food items
    if foodItemIndexes == []:
        newFoodID = foodCategoryName[0] + '1'
        for data in foodItemsList:
            if foodCategoryName.upper() == data[0][0:len(foodCategoryName)]:
                lastFoodItemIndex = foodItemsList.index(data) + 1
    # #Assigns a new food ID by adding 1 to the last food item ID in the food category
    else: 
        lastFoodItemIndex = foodItemIndexes[-1]
        lastFoodItemRecord = foodItemsList[lastFoodItemIndex][0].split(" | ")
        newFoodID = lastFoodItemRecord[0][0] + (str(int(lastFoodItemRecord[1][1])+1))
    #If the food item index is equivalent to the last food item in the file, a new line is appended before the new data to prevent additional newlines in the file
    if (lastFoodItemIndex == (len(foodItemsList)-1)):
        foodItemsList.insert(lastFoodItemIndex+1, [f'\n{foodCategoryName} | {newFoodID} | {foodItemName} | {foodItemPrice}'])
    else:
        foodItemsList.insert(lastFoodItemIndex+1, [f'{foodCategoryName} | {newFoodID} | {foodItemName} | {foodItemPrice}\n'])
    #Writes the updated foodItemsList into the food details file
    with open ("./foodDetails.txt", mode='w') as foodDetailsFile:
        for data in foodItemsList:       
            foodDetailsFile.write(data[0])
    print(" Success!")


'''Modify food item'''
def modifyFoodItemMenu(): #Function that displays main page for admins to modify records of food items
    foodDetailsList = []
    with open("./foodDetails.txt", mode='r') as foodDetailsFile:
        for row in foodDetailsFile:
            foodDetailsList.append([row])
    print("\nWhat update do you intend to perform?")
    print("\n1. Update Record","2. Delete Record","\n0. Back to Admin Menu", sep='\n')
    #Redirects user based on chosen options
    while True:
        try:
            modifyChoice = int(userInput("\nI would like to (Number) ",False))
            if modifyChoice == 0:
                adminMenu()
            elif modifyChoice == 1:
                clearConsole()
                pageBanners("UPDATE FOOD ITEM", 50)
                updateFoodItemMenu(foodDetailsList)
                time.sleep(0.5)
                adminMenu()
            elif modifyChoice == 2:
                clearConsole()
                pageBanners("DELETE FOOD ITEM", 50)
                deleteFoodItemMenu(foodDetailsList)
                time.sleep(0.5)
                adminMenu()
            else:
                print("\nERROR: Number is out of range")
                continue
            break
        except ValueError:
            print("\nERROR: Foreign character submitted")

def verifyFoodItemId(foodItemId:str, foodDetailsList:list) -> bool: #Function that verifies the format and existence of the food item ID that has been received by the user, update pseudocode
    if foodItemId == '' : 
        return False
    elif (foodItemId[0].isalpha() and foodItemId[1: len(foodItemId)].isdigit()):
        for data in foodDetailsList:
            if foodItemId in data[0]:
                return True
    else:
        return False

def verifyFoodCategoryNumber() -> bool: #Function that verifies that the food category number submitted fulfills formats determined
    validCategoryNumber = False
    foodCategoryTitles = extractFoodCategoryTitles()
    while (not validCategoryNumber):
        try:
            categoryNumber = int(userInput("Food category number",True))
            if 0 < categoryNumber <= len(foodCategoryTitles):
                validCategoryNumber = True
                listOutFoodItems(foodCategoryTitles[categoryNumber-1][0])
            elif categoryNumber == 0:
                adminMenu()
            else:
                print("ERROR: Food category number out of range")
        except ValueError:
            print("ERROR: Foreign character submitted")
    return validCategoryNumber

def listOutFoodItems(chosenFoodCategoryName:str): #Function that displays the details of all food items in the food details file based on the category chosen by the user, pseudocode TBC
    foodItemDetails = readFoodDetailsFile()
    progressBar("Retrieving food item records")
    time.sleep(0.5)
    print(f"\n\nREPORT OF FOOD ITEMS IN {chosenFoodCategoryName.upper()}\n{'-'*24}{'-'*len(chosenFoodCategoryName)}")
    print(f"FOOD ITEM ID\tFOOD ITEM PRICE\t FOOD ITEM NAME\n{'-'*12}{' '*4}{'-'*15}{' '*2}{'-'*14}")
    for data in foodItemDetails:
        if (chosenFoodCategoryName.replace("FOOD CATEGORY", "").strip().capitalize()) in data:
            print('{:<16}{:<15}\t {}'.format(data[1],data[3],data[2]))
        

def updateFoodItemMenu(foodDetailsList:list): #Function that displays menu for user to choose which specific food item id they want to update
    print("\nIn which category would you like to update the food item?\n")
    displayFoodCategories()
    print("\n0. Back to Admin Menu")
    validCategoryNumber = verifyFoodCategoryNumber()
    #Asks user to specify which food item id from selected category to be updated
    while (validCategoryNumber):
        foodItemId = userInput("Enter the Food Item ID that you would like to update",True).upper()
        if (verifyFoodItemId(foodItemId, foodDetailsList)):
            print(f"Food item ID selected: {foodItemId}")
            #Get specific list and list index of food items from the main data list
            for data in foodDetailsList:
                if foodItemId in data[0]:
                    foodItemIdList = data[0].split(" | ")
                    foodItemIdIndex = foodDetailsList.index(data)              
            updateFoodItemRecord(foodDetailsList, foodItemIdList, foodItemIdIndex)
            break
        else:
            print("ERROR: Invalid Food Item ID")

def deleteFoodItemMenu(foodDetailsList:list): #Function that displays menu for user to choose which specific food item ID they want to delete
    print("\nIn which category would you like to delete the food item?\n")
    displayFoodCategories()
    print(f"\n0. Back to Admin Menu")
    validCategoryNumber = verifyFoodCategoryNumber()
    validUserConfirmation = False
    while (validCategoryNumber):
        foodItemId = userInput("Enter the Food Item ID that you would like to delete",True).upper()
        if(verifyFoodItemId(foodItemId,foodDetailsList)):
            print(f"Are you sure you want to delete {foodItemId}?")
            while (not validUserConfirmation):
                userConfirmation = userInput("(Y)es/(N)o",True).upper()
                if (userConfirmation in ('Y', 'N')):
                    validUserConfirmation = True
                    validCategoryNumber = False
                    deleteFoodItemRecord(userConfirmation, foodItemId, foodDetailsList)
                else:
                    print("Invalid input")
        else:
            print("Invalid Food Item ID")
        


def updateFoodItemRecord(foodDetailsList:list, foodItemIdList:list, foodItemIdIndex:int): #Function that updates a specific record of food item in the food details text file
    validUpdateChoice = False
    print("\nWhat would you like to update?","1. Food Item Price","2. Food Item Name","3. Both",sep='\n')
    while not validUpdateChoice:
        try:
            updateCriteria = int(userInput("Update choice",True))
            if updateCriteria <= 0 or updateCriteria > 3:
                print("ERROR: Out of range")
            else:
                validUpdateChoice = True
        except ValueError:
            print("ERROR: Foreign character submitted")
    while validUpdateChoice:
        try:
            if updateCriteria == 1:
                newPrice = userInput("New food item price",False)
                newPrice = format(float(newPrice),'.2f')
                foodItemIdList[3] = f'{newPrice}\n' if '\n' in foodItemIdList[3] else '{newPrice}'
            if updateCriteria == 2:
                foodItemIdList[2] = f'{userInput("New food item name",False)}'
            if updateCriteria == 3:
                newPrice = userInput("New food item price",False)
                newPrice = format(float(newPrice),'.2f')
                foodItemIdList[2] = f'{userInput("New food item name",False)}'
                foodItemIdList[3] = f'{newPrice}\n' if '\n' in foodItemIdList[3] else '{newPrice}'
        except ValueError:
            print("\nERROR: Foreign character submitted")
            continue
        break
    progressBar("Making changes")
    foodDetailsList[foodItemIdIndex] = [" | ".join(foodItemIdList)]
    with open("./foodDetails.txt", mode='w') as f:
        for data in foodDetailsList:
            f.write(data[0])
    print(" Success!")
    time.sleep(0.2)

def deleteFoodItemRecord(userConfirmation:str, foodItemId:str, foodDetailsList:list): #Function that deletes a specific food item record in the food details text file
    while True:
        if (userConfirmation=="Y"):
            #Removes the sublist of the food item that contains the food item id from the main list
            progressBar(f"Deleting {foodItemId}")
            for data in foodDetailsList:
                if foodItemId in data[0]:
                    foodDetailsList.pop(foodDetailsList.index(data))
                #If last food item in the file has a newline, it is removed
                if '\n' in foodDetailsList[-1][-1]:
                    foodDetailsList[-1][-1] = foodDetailsList[-1][-1].strip("\n")
            with open ("./foodDetails.txt",mode='w') as f:
                for data in foodDetailsList:
                    f.write(data[0])
            print(" Success!")
            break
        else:
            adminMenu()
            
'''Main Menu Page for Display'''
def readOrderRecordsFile() -> list: #Function that reads file with order records, extract order records without headers and append to list
    orderDetailsList = []
    with open("./orderRecords.txt", mode='r') as orderRecordsFile:
        skipFileLine(6,orderRecordsFile)
        for row in orderRecordsFile:
            orderDetailsList.append(row.strip('\n').split(" | "))
    return orderDetailsList

def extractFoodCategoryTitles(): #Function that gets the title and description of the food categories ONLY from the food details text file and append it to list
    rawList = []
    foodCategoryDetails = []
    #rawList stores food category titles, descriptions and food items too
    with open ("./foodDetails.txt", mode='r') as foodDetailsFile:
        skipFileLine(4,foodDetailsFile)
        for line in foodDetailsFile:
            rawList.append(line.strip().replace('_','').split(","))
    #Remove food items only from rawList
    for data in removeEmptyList(rawList):
        if " | " in data[0]:
            rawList.pop(rawList.index(data))
    #Splits food category name and description according to the position of '-'
    for list in removeEmptyList(rawList):
        for data in list:
            for i in range(len(data)):
                if data[i] == "-":
                    foodCategoryDetails.append([''.join(data[0:i-1]),''.join(data[i+2:-1])])
    return foodCategoryDetails       

def displayRecordsMenu(): #Function to display records main page
    validCategoryNumber = False
    foodCategoryList = extractFoodCategoryTitles()
    print("\n1. Food Categories","2. Food Items by Category","3. Customer Orders","4. Customer Payment","\n0. Back to Admin Menu", sep='\n')
    OPTIONS = [[1, displayFoodCategoryRecords], [3, displayOrderOrPaymentRecords],
              [4, displayOrderOrPaymentRecords]]
    while not validCategoryNumber:
        try:
            userSelection = int(userInput("Display (Number)",True))
            validCategoryNumber = True
        except ValueError:
            print("ERROR: Please enter a number")
            time.sleep(0.1)
    
    while validCategoryNumber:
        try:
            if userSelection == 1:
                progressBar("Generating report")
                OPTIONS[0][1]()
                print("\nRedirecting to admin menu in 15 seconds...")
                time.sleep(15)
                adminMenu()
            elif userSelection == 2 :
                print("\nSelect the food category that you want to be displayed\n")
                displayFoodCategories()
                chosenCategory = int(userInput("Category number",True))
                listOutFoodItems((foodCategoryList[chosenCategory-1][0]))
                print("\nRedirecting to admin menu in 15 seconds...")
                time.sleep(15)
                adminMenu()
            elif userSelection == 3:
                progressBar("Generating report")
                OPTIONS[1][1]('orders')
                print("\nRedirecting to admin menu in 15 seconds...")
                time.sleep(15)
                adminMenu()
            elif userSelection == 4:
                progressBar("Generating report")
                OPTIONS[2][1]('payments')
                print("\nRedirecting to admin menu in 15 seconds...")
                time.sleep(15)
                adminMenu()
            elif userSelection == 0 :
                adminMenu()
            else:
                raise TypeError
        except ValueError:
            print("ERROR: Please enter a number")
            time.sleep(0.1)
        except TypeError:
            print("ERROR: Number out of range")
            time.sleep(0.1)
            continue
        break

def displayFoodCategoryRecords(): #Function that displays the records of food categories and descriptions cleanly
    foodCategoryList = extractFoodCategoryTitles()
    '''Print data in user readable form'''
    print(f'\n\t\tDETAILS OF FOOD CATEGORIES\n\t\t{"-"*26}')
    print(
        f"CATEGORY NAME(S)\t\tCATEGORY DESCRIPTION(S)\n{'-'*15}\t\t\t{'-'*22}")
    for data in foodCategoryList:
        print('{:<32}{}'.format(data[0], data[1]))


def displayOrderOrPaymentRecords(displayChoice:str): #Function that displays either order or payment records based on parameters given 
    orderRecordsList = readOrderRecordsFile()
    print(f"\n\t\t\t\tREPORT OF ALL CUSTOMER {displayChoice.upper()}\n\t\t\t\t{'-'*31}\n")
    if displayChoice == 'orders':
        print(
            f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID (QUANTITY)\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*12}{' '*4}{'-'*18}")
        for data in orderRecordsList:
            print('{:<24}{:<16}{:<16}{:<16}{}'.format(
                data[0], data[1], data[3], data[7], data[2]))
    else:
        print(
            f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\tPAID ON\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*14}{' '*2}{'-'*14}{' '*2}{'-'*7}")
        for data in orderRecordsList:
            print('{:<24}{:<16}{:<16}{:<16}{:<16}{}'.format(
                data[0], data[1], data[3], data[4], data[5], data[6]))


'''Search Menu Main Page'''
def searchPageHeader(section:str): #Standard header for search page 
    clearConsole()
    pageBanners(section, 50)
    print("\nOn what basis should the records be searched?".center(100))
    print("\n1. Customer Username","2. Order ID", "\n0. Back to Admin Menu\n", sep='\n')


def searchRecordsMenu(): #Main page for users to select type of record search
    orderRecordsList = readOrderRecordsFile()
    print("\nWhich record do you want to check?")
    print("\n1. Customer Order Record","2. Customer Payment Record","\n0. Back to Admin Menu\n", sep='\n')
    validSearchCategory = False
    validSearchCriteria = False
    while (not validSearchCategory):
        try:
            searchCategory = int(userInput("Search(Number)",False))
            if searchCategory == 1:
                searchPageHeader("SEARCH CUSTOMER ORDER")
                validSearchCategory = True
            elif searchCategory == 2:
                searchPageHeader("SEARCH CUSTOMER PAYMENT")
                validSearchCategory = True
            elif searchCategory == 0:
                adminMenu()
            else:
                print("\nERROR: Number submitted is outside allowed range")
                validSearchCategory = False
        except ValueError:
            print("\nERROR: Please enter a number")
    while not validSearchCriteria:
        try:
            searchCriteria = int(userInput("Search(Number)",False))
            if searchCategory == 1:
                if searchCriteria == 1:
                    searchOrderByUsername(orderRecordsList)
                    validSearchCriteria = True
                elif searchCriteria == 2:
                    searchOrderById(orderRecordsList)
                    validSearchCriteria = True
                elif searchCriteria == 0:
                    adminMenu()
                else: 
                    print("ERROR: Number submitted is outside allowed range")
            if searchCategory == 2:
                if searchCriteria == 1:
                    searchPaymentByUsername(orderRecordsList)
                    validSearchCriteria = True
                elif searchCriteria == 2:
                    searchPaymentById(orderRecordsList)
                    validSearchCriteria = True
                else: 
                    print("\nERROR: Number submitted is outside allowed range")
        except ValueError:
            print("\nERROR: Please enter a number")


'''Search Specific Customer Order Record'''
def searchOrderByUsername(orderRecordsList:list): #Search customer order by username
    validUsername = False
    recordByUsername = []
    count = 0
    while not validUsername:
            username = userInput("Please enter Customer Username",True)
            if username.isdigit() or username == "":
                print("ERROR: Invalid username")
            else:
                validUsername = True
    while validUsername:
        for data in orderRecordsList:
            if (username.lower() == data[0]):
                recordByUsername.append(
                    [data[0], data[1], data[2], data[3], data[7]])
                count += 1
        if count >= 1:
            print("{} order records have been found for {}".format(count, username))
            progressBar("Generating report")
            time.sleep(0.5)
            displaySearchResults('orders', username, recordByUsername)
        else:
            print("No order records found for {}".format(username))
        break
    

def searchOrderById(orderRecordsList:list): #Search customer order by Order ID
    validOrderId = False
    recordById = []
    orderExists = False
    while not validOrderId:
        orderID = str(userInput("Please enter Order ID",True)).upper()
        if orderID == "":
            print("ERROR: Please submit an order ID")
        elif orderID[0] != 'O':
            print("ERROR: Order ID should start with an "'O'"")
        elif not(orderID[0].isalpha() and orderID[1:len(orderID)].isdigit()):
            print("ERROR: Invalid Order ID format")
        else:
            validOrderId = True
    while validOrderId:
        for data in orderRecordsList:
            if (orderID.upper() in data):
                recordById.append([data[0],data[1],data[2],data[3],data[7]])
                orderExists = True
        if (orderExists):
            print("1 Order record have been found for Order ID {}".format(orderID.upper()))
            progressBar("Generating report")
            time.sleep(0.5)
            displaySearchResults('orders',orderID,recordById)
        else:
            print("No order records found for {}".format(orderID.upper()))
        break
    
'''Search Specific Customer Payment Record'''
def searchPaymentByUsername(paymentList:list): #Search customer order by Username
    validUsername = False
    recordByUsername = []
    count = 0
    while not validUsername:
            username = userInput("Please enter Customer Username",True)
            if username.isdigit() or username == "":
                print("ERROR: Invalid username")
            else:
                validUsername = True
    while validUsername:
        for data in paymentList:
            if (username.lower() == data[0]):
                recordByUsername.append(
                    [data[0], data[1], data[3], data[4], data[5], data[6]])
                count += 1
        if count >= 1:
            print("{} payment records have been found for {}".format(count, username))
            progressBar("Generating report")
            time.sleep(0.5)
            displaySearchResults('payments', username, recordByUsername)
        else:
            print("No payment records found for {}".format(username))
        break

def searchPaymentById(paymentList:list): #Search customer order by Order ID
    validOrderId = False
    recordById = []
    orderIdExists = False
    while not validOrderId:
        orderID = str(userInput("Please enter Order ID",True)).upper()
        if orderID == "":
            print("ERROR: Please submit an order ID")
        elif orderID[0] != 'O':
            print("ERROR: Order ID should start with an "'O'"")
        elif not(orderID[0].isalpha() and orderID[1:len(orderID)].isdigit()):
            print("ERROR: Invalid Order ID format")
        else:
            validOrderId = True
    while validOrderId:
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
        break


'''Display Search Results'''
def displaySearchResults(recordName:str,searchBasis:str,resultsList:list): #Function that gets search results from the earlier search functions and displays it cleanly
    if recordName == 'orders':
        print(
            f"\n\t\t\t\tORDER REPORT FOR {searchBasis.upper()}\n\t\t\t\t{'-' * len(searchBasis)}{'-'*17}\n")
        print(
            f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tORDER STATUS\tFOOD ID(QUANTITY)\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*12}{' '*4}{'-'*17}")
        for data in resultsList:
            print('{:<24}{:<16}{:<16}{:<16}{}'.format(
                data[0].upper(), data[1], data[3], data[4], data[2]))
    else:
        print(
            f"\n\t\t\t\tPAYMENT REPORT FOR {searchBasis.upper()}\n\t\t\t\t{'-'*19}{'-' * len(searchBasis)}\n")
        print(
            f"CUSTOMER USERNAME\tORDER ID\tTOTAL PAYABLE\tPAYMENT METHOD\tPAYMENT STATUS\tPAID ON\n{'-'*17}{' '*7}{'-'*8}{' '*8}{'-'*13}{' '*3}{'-'*14}{' '*2}{'-'*14}{' '*2}{'-'*7}")
        for data in resultsList:
            print('{:<24}{:<16}{:<16}{:<16}{:<16}{}'.format(data[0].upper(),data[1],data[2],data[3],data[4],data[5]))  
    print("\nRedirecting to admin menu in 15 seconds...")
    time.sleep(15)
    adminMenu()

#==================================USER SECTION===============================================

# User homepage
# User menu for viewing guest menu, login, register.
def userHomepage(): 
    while True:
        clearConsole()
        pageBanners("GUEST DASHBOARD", 50)
        print("\nPlease select any option below.")
        print("1. View Menu", "2. Customer Login",
              "3. New Customer Registration", "\n0. Back to Main Menu", sep='\n')
        input = userInput("Choice", True).strip()
        if input == "1":
            guestMenu()
        elif input == "2":
            customerMenu(customerLoginMenu())
        elif input == "3":
            pageBanners("NEW ACCOUNT", 50)
            customerRegistrationMenu()
        elif input == "0":
            break
        else:
            input("ERROR: Invalid selected number.")

# Guest Menu
# Allow user to view categories without details and choose item cat to display.
def guestMenu():
    while True:
        clearConsole()
        pageBanners("MENU CATEGORIES", 50)
        print("\n")
        displayFoodCategories()
        print("\n0. Back To Guest Menu")
        try:
            print("\nSelect the food category that you want to be displayed")
            chosenCategory = int(userInput("Food category", True).strip())
            if chosenCategory == 0:
                break
            elif chosenCategory <= 4 :
                guestPrintItem((extractFoodCategoryTitles()[chosenCategory-1][0]))
            else :
                input("ERROR: Invalid chosen category.")
        except ValueError:
            input("ERROR: Please enter numbers only.")

# Print items without detail.
def guestPrintItem(chosenFoodCategoryName):
    while True:
        try:
            clearConsole()
            print(f"FOOD ITEMS IN {chosenFoodCategoryName.upper()}\n{'-'*24}{'-'*len(chosenFoodCategoryName)}")
            for data in readFoodDetailsFile():
                if (chosenFoodCategoryName.replace("FOOD CATEGORY", "").strip().capitalize()) in data:
                    print(data[2])
            input("\nPress Enter to Return")
            break
        except TypeError:
            input("ERROR: Please enter numbers only.")


# Customer login page.
def customerLoginMenu():
    while True:
        clearConsole()
        pageBanners("Login as Customer", 50)
        try:
            customerDetailsList = customerReadDetailFile()
            uName = userInput("Username", True).strip()
            progressBar("Checking if username exists")
            if (authUsername(uName, customerDetailsList)):
                print("Username found, please enter password\n")
                while True:
                    uPass = userInput("Password", True).strip()
                    if (authPassword(uName, uPass, customerDetailsList)):
                        progressBar("Logging you in")
                        return uName
                    else:
                        print("Incorrect password, please retry\n")
            else:
                print("Username not found, please retry")
        except TypeError:
            input("ERROR: Customers details file is corrupted!")
            break

# Read customer detail file.
def customerReadDetailFile() -> list:
    customerDetailsList = []
    with open("./customerDetails.txt", mode='r') as customerDetailsFile:
        skipFileLine(6, customerDetailsFile)
        for row in customerDetailsFile:
            customerDetailsList.append(
                row.strip("\n").replace(" | ", " ").split(" "))
    return customerDetailsList

# Category Menu
# Customer menu allow user to choose categories with details to view, view histrorical orders and logout.
def customerMenu(username: str):
    cart = []
    while True:
        try:
            clearConsole()
            pageBanners("Customer Menu", 50)
            print("\nWelcome!, what would you like to do today?")
            print("1. View Item By Categories", "2. View Orders", "\n0. Logout", sep='\n')
            input = int(userInput("Choice", True).strip())
            if input == 1:
                cart = customerMenuCategory(cart, username)
            elif input == 2:
                customerOrderMenu(username)
            elif input == 0:
                break
            else:
                input("\nERROR: Number out of rang.")
        except ValueError:
            input("\nERROR: Please enter a valid selection number.")

# Customer category menu that allow user to choose which category of items to print.
def customerMenuCategory(cart: list, username:str):
    foodCat = extractFoodCategoryTitles()
    foodCatLen = len(foodCat)
    while True:
        try:
            clearConsole()
            pageBanners("Food Menu", 50)
            print("\nWhat category of beverage would you like to know more?\n")
            customerPrintCategoryDetail()
            if len(cart) > 0:
                customerCartPrint(cart)
            print("\nC. View Cart\n0. Back to Customer Menu")
            chosenCategory = userInput("Food category", True).strip()
            if chosenCategory == "0":
                return cart
            elif chosenCategory.upper() == "C":
                customerCartMenu(cart, username)
                cart = []
            elif int(chosenCategory) <= foodCatLen:
                cart = customerItemMenu(cart, (extractFoodCategoryTitles()[int(chosenCategory)-1][0]))
            else:
                input("\nERROR: Number out of range.")
        except ValueError:
            input("\nERROR: Please enter a valid selection number.")

# Print Categories with detail.
def customerPrintCategoryDetail():
    foodCat = extractFoodCategoryTitles()
    for i in range(len(foodCat)):
        print("{}. {} - {}".format(i+1, foodCat[i][0], foodCat[i][1]))

# Cart system
# Customer cart menu for checkup current cart and proceed to checkout or back.
def customerCartMenu(cart: list, username: str):
    while True:
        clearConsole()
        pageBanners("  Cart  ", 50)
        cartDetailArray, cartTtl = customerCartDetail(cart)
        print("\n{:<3}{:<2}{:<32}{:<2}{:<9}{:<2}{:<11}{:<2}{:<17}{:<2}".format(
            "N", "|", "Item Name", "|", "Quantity", "|", "Unit Price", "|", "Total Unit Price", "|"))
        print("{:<3}{:<2}{:<32}{:<2}{:<9}{:<2}{:<11}{:<2}{:<17}{:<2}".format(
            "", "|", "", "|", "", "|", "", "|", "", "|"))
        for i in range(len(cartDetailArray)):
            print("{:<3}{:<2}{:<32}{:<2}{:<9}{:<2}{:<11}{:<2}{:<17}{:<2}".format((str(i+1)+"."), "|",
                  cartDetailArray[i][0], "|", cartDetailArray[i][1], "|", cartDetailArray[i][2], "|", cartDetailArray[i][3], "|"))
        print(f"\nTotal: {cartTtl}\n\n1. Submit Order Cart\n0. Back")
        option = userInput("Choice", True).strip()
        if option == "0":
            break
        elif option == "1":
            customerCartSubmit(cart, username, cartTtl)
            return ([])
        else:
            print("ERROR: Something went wrong, invalid input.")

# Return item names, quantity, unit price and total of cart in a list.
def customerCartDetail(cart: list):
    itemsArray = readFoodDetailsFile()
    cartDetail = []
    cartTotal = 0
    for cartItem in range(0, len(cart), 2):
        for item in range(len(itemsArray)):
            if cart[cartItem] == itemsArray[item][1]:
                unitTotal = (
                    float(itemsArray[item][3])*float(cart[cartItem+1]))
                cartTotal += unitTotal
                # detail = Item Name, Quantity, Unit Price, Total Unit Price
                detail = [(itemsArray[item][2]), str(cart[cartItem+1]),
                          itemsArray[item][3],  str(unitTotal)]
                cartDetail.append(detail)
    cartTotal = "{:.2f}".format(cartTotal)
    return (cartDetail, cartTotal)

# Append order details to oder file.
def customerCartSubmit(cart: list, username: str, cartTtl: float):
        if len(cart) == 0:
            input("ERROR: Your order cart is empty.")
            return
        itemString = ""
        for i in range(0, len(cart), 2):
            itemString += cart[i] + "(" + str(cart[i + 1]) + ")"
            if i < (len(cart)-2):
                itemString += ","
        record = username + " | " + str(customerOrderDetailFileLen()+1) + " | " + itemString + " | " + str(cartTtl) + " | " + "PAID\n"
        with open("./orderRecords.txt", "a") as orderFile:
            orderFile.write(record)
        input("Order placed successfully, please press enter to return.")

# Return numbers of order in order file.
def customerOrderDetailFileLen():
    len = 0
    with open("./orderRecords.txt", mode='r') as orderDetailFile:
        skipFileLine(6, orderDetailFile)
        for row in orderDetailFile:
            len += 1
    return len

# Ordering System
# Customer menu for choosing what item to add to cart.
def customerItemMenu(cart: list, chosenFoodCategoryName: str) -> list:
    cartChosen, addCartChosen = False, False
    while True:
        clearConsole()
        customerItemPrint(chosenFoodCategoryName)
        try:
            cart = customerCartTidy(cart)
            if len(cart) > 0:
                customerCartPrint(cart)
        except TypeError:
            print()
        if cartChosen:
            if addCartChosen:
                itemToAdd = userInput("Item Code to Add (M2)", True).strip().upper()
                if customerCartValidItem(itemToAdd):
                    amountToAdd = str(userInput("Amount", True).strip())
                    cart = customerCartAddItem(itemToAdd, amountToAdd, cart)
                    cartChosen, addCartChosen = False, False
                else:
                    input("\nERROR: Invalid amount input.")
                    cartChosen, addCartChosen = False, False
            else:
                itemToRemove = userInput("Item code to remove", True).strip().upper()
                if customerCartValidItem(itemToRemove):
                    amountToRemove = userInput("Amount to Remove (\"All\" to remove item from cart)", True).strip()
                    cart = customerCartRemoveItem(itemToRemove, amountToRemove, cart)
                    cartChosen = False
                else:
                    input("ERROR: Invalid amount input.")
                    cartChosen = False
        else:
            print("\n1. Add Item to Cart.\n2. Remove Item from Cart.\n\n0. Back")
            uInput = userInput("Choice", True).strip().upper()
            if uInput == "0":
                return cart
            elif uInput == "1":
                cartChosen, addCartChosen = True, True
            elif uInput == "2":
                cartChosen = True
            else:
                input("ERROR: Invalid selection entered.")

# Print items with details.
def customerItemPrint(chosenFoodCategoryName: str):
    while True:
        try:
            print(f"{chosenFoodCategoryName.upper()}".center(50))
            print(f"{'-'*24}{'-'*len(chosenFoodCategoryName)}")
            print(
                f"FOOD ITEM ID\tFOOD ITEM PRICE\t FOOD ITEM NAME\n{'-'*12}{' '*4}{'-'*15}{' '*2}{'-'*14}")
            for data in readFoodDetailsFile():
                if (chosenFoodCategoryName.replace("FOOD CATEGORY", "").strip().capitalize()) in data:
                    print('{:<16}{:<15}\t {}'.format(
                        data[1], data[3], data[2]))
            break
        except TypeError:
            input("ERROR: Please enter a number.")

# Remove item code from list which quantity equivalent to 0 to less.
def customerCartTidy(cart: list) -> list:
    tempCart = []
    for i in range(0, len(cart), 2):
        if cart[i+1] != 0:
            tempCart.extend([cart[i], cart[i+1]])
    return tempCart

# Print item code and quantity in cart. (Cart: M1(x), W2(x))
def customerCartPrint(cart: list):
    stringToPrint = ""
    for i in range(0, len(cart), 2):
        stringToPrint = stringToPrint + cart[i] + "(" + str(cart[i+1]) + ")"
        if i < (len(cart)-2):
            stringToPrint = stringToPrint + ", "
    print(f"\nCart :  {stringToPrint}")

# Validate if item code exist in menu.
def customerCartValidItem(code: str) -> bool:
    itemsArray = readFoodDetailsFile()
    for item in range(len(itemsArray)):
        if itemsArray[item][1] == code:
            return True
    return False

# Add item with quantity to list.
def customerCartAddItem(item: str, amount: str, cart: list) -> list:
    try:
        intAmount = int(amount)
        for i in range(0, len(cart), 2):
            if cart[i] == item:
                cart[i+1] += intAmount
                return cart
        cart.extend([item, intAmount])
        return cart
    except:
        input("\nERROR: Alphabet/s found in amount entered, please enter numbers only.")
        return cart

# Deduct item quantity from cart.
def customerCartRemoveItem(item: str, amount: str, cart: list):
    if amount.upper() != "ALL":
        try:
            intAmount = int(amount)
        except:
            input("ERROR: Invalid string found, do you mean \"All\"?")
            return cart
    for i in range(0, len(cart), 2):
        if cart[i] == item:
            amountFromCart = cart[i+1]
            if amount.lower() == "all":
                cart[i+1] = 0
            elif intAmount <= amountFromCart:
                cart[i+1] -= intAmount
            elif intAmount > amountFromCart:
                input("ERROR: Amount entered is too large.")
                return cart
            return cart
    input("ERROR: Item code entered not found, please try again.")
    return cart

# Order History
# Customer order menu for printing current user's historical orders.
def customerOrderMenu(username: str):
    clearConsole()
    pageBanners("  Orders  ", 50)
    print("")
    customerOrderPrint(username)
    input("\nPress enter to return.")

# Print historical orders of current user.
def customerOrderPrint(username: str):
        orderDetailArray = customerOrderDetailRead(username)
        print("{:<9}{:<2}{:<32}{:<2}{:<8}{:<2}{:<7}{:<2}".format(
            "Order ID", "|", "Items", "|", "Total", "|", "Status", "|"))
        print("{:<9}{:<2}{:<32}{:<2}{:<8}{:<2}{:<7}{:<2}".format(
            "", "|", "", "|", "", "|", "", "|"))
        for i in range(len(orderDetailArray)):
            print("{:<9}{:<2}{:<32}{:<2}{:<8}{:<2}{:<7}{:<2}".format(
                orderDetailArray[i][1], "|", orderDetailArray[i][2], "|", orderDetailArray[i][3], "|", orderDetailArray[i][4], "|"))

# Read order details from orders detail file.
def customerOrderDetailRead(username: str):
    orderArray = []
    with open("./orderRecords.txt", mode='r') as orderDetailFile:
        skipFileLine(6, orderDetailFile)
        for row in orderDetailFile:
            order = row.strip("\n").replace(" | ", " ").split(" ")
            if order[0] == username:
                orderArray.append(order)
    return orderArray

# Customer Registration 
# Customer registration menu for user account registration.
def customerRegistrationMenu():
    titleList = ["Username", "Password", "First Name", "Last Name", "House Number", "Street", "State", "Postcode", "Phone Number"]
    userData = ["", "", "", "", "", "", "", "", ""]
    while True:
        for a in range(len(titleList)):
            clearConsole()
            pageBanners("Registration", 50)
            print("")
            for b in range(9):
                print("{:<15}{:<2}{:<2}".format(titleList[b], ":", userData[b]))
            print("\n0. Type \"0\" to cancel registration.")
            data = userInput(titleList[a], True).strip()
            if data == "0":
                return
            userData[a] = data
        success = customerRegistrationSubmit(userData)
        if success:
            input("\nUser account regsitered successfully, please enter to return.")
            break

# Add registration data to users detail file.
def customerRegistrationSubmit(userData:list):
    for data in userData:
        if data.strip() == "":
            input("ERROR: An empty data found, please try again.")
            return False
        record = userData[0] + " | " + userData[1] + " | " + userData[2] + " | " + userData[3] + " | " + userData[4] + " | " + userData[5] + " | " + userData[6] + " | " + userData[7] + " | " + userData[8] + "\n"
    with open("./customerDetails.txt", "a") as custFile:
        custFile.write(record)
    return True
    

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
        print("\nWho are you logging in as?\n", "1. Admin", "2. Customer", "3. Quit Program", sep=' \n')
        try:
            uInput = int(userInput("Login as (Number)",True).strip())
            if uInput == 1 :
                clearConsole()
                pageBanners("ADMIN LOGIN PAGE", 50)
                adminLoginPage()
            elif uInput == 2:
                userHomepage()
            elif uInput == 3:
                quit()
            else:
                input("ERROR: Number out of choice range")
        except ValueError:
            input("ERROR: Foreign character submitted")
            

'''EXECUTE MAIN'''
if __name__ == '__main__':
    try:
        initialProgramCheck()
        progressBar("\nLoading program")
        time.sleep(0.1)
        main()
    except KeyboardInterrupt:
        quit()