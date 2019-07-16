#Grocery Shopping Experience
groceryList = []
name = ""

#--------------- Functions
def MainMenu():
    command = input("\nWhat would you like to do today? \n(1) Start new list (2) Edit list (3) View list (4) Shop ")
    command = int(command)

    if command == 1:
        #Starting List...
        StartList()
    elif command == 2:
        if len(groceryList) == 0:
            cont = input("Your list is empty! Start a new list? \n(y) or (n) ")
            if cont == "y":
                StartList()
            else:
                MainMenu()
        else:
            #Editing list...
            ChangeList()
    elif command == 3:
        #Printing list...
        PrintList(False)
    elif command == 4:
        #Shopping Experience...
        Shop()


def StartList():
    print ("Starting new list...")
    end = False
    while end == False:
        item = input("Enter item name: ")
        groceryList.append(item)
        cont = input("Add another item? \n(y) or (n) ")
        if cont == "n":
            end = True
            MainMenu()

def ChangeList():
    print("Editing your list...")
    end = False
    PrintList(True)
    while end == False:
        addRem = input("Would you like to (a) add an item, (r) remove an item, or (m) return to menu? ")
        if addRem == "r":
            while end == False:
                edit = input("Enter index of item for removal: ")
                edit = int(edit)
                groceryList.pop(edit)
                PrintList(True)
                cont = input("Remove another item? \n(y) or (n) ")
                if cont == "n":
                    break
        elif addRem == "a":
            while end == False:
                edit = input("Enter item name: ")
                groceryList.append(edit)
                PrintList(True)
                cont = input("Add another item? \n(y) or (n) ")
                if cont == "n":
                    break
        elif addRem == "m":
            end = True
            MainMenu()

def PrintList(bol):
    print("Printing your list...\n")
    i = 0
    print(name, "'s Grocery List: ")
    for item in groceryList:
        print(i, item)
        i +=1
    print("")
    if bol == False:
        MainMenu()

def Shop():
    if len(groceryList) == 0:
        print("Your grocery list is empty! ")
        MainMenu()
    else:
        print("Initiating shopping experience...")
        print("Lo is gathering your items...")
        for item in groceryList:
            print("Finding...")
            print(item, " Found! - Removed from list")
            print("")
        for item in groceryList:
            groceryList.remove(item)
        print("All items collected - Shopping List is now empty.")
        print("Thank you for shopping with Lo, your personal grocery shopping assistant!\n")


#--------------- Functions END

name = input("Welcome. Please enter your name: ")
print ("Hello " + name + ", I am Lo, your personal grocery shopping assistant")
MainMenu()
