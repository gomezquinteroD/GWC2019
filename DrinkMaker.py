#Made by Daniela Gomez-Quintero


cup = ''
drinkType = ''
HotIced = ''
drinkSpecial = ''
print("Welcome to Make Your Own Drink!")
print("First, pick a size:")
user1 = input("Tall, Grande, or Venti \n")
if (user1 == "Tall"):
    print("You picked a Tall cup")
    cup = "Tall"
if (user1 == "Grande"):
    print("You picked a Grande cup")
    cup = "Grande"
if (user1 == "Venti"):
    print("You picked a Venti cup")
    cup = "Venti"

print("What kind of drink would you like?")
user2 = input("(1) Coffee, (2) Tea, (3) Frappuccino, (4) Other \n")
if (user2 == "1"):
    print("You picked coffee.")
    drinkType = "Coffee"
    coffee1 = input("Would you like (1) hot or (2) iced coffee? \n")
    if (coffee1 == "1"):
        print("You picked hot coffee.")
        hotIced = "Hot"
        print("Pick a hot coffee:")
        coffee2 = input("(1) Americano \n(2) Brew \n(3) Cappuccino \n(4) Espresso \n(5) Flat White \n(6) Latte \n(7) Macchiato \n(8) Mocha \n")
        if (coffee2 == "1"):
            drinkSpecial = "Americano"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "2"):
            drinkSpecial = "Brew"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "3"):
            drinkSpecial = "Cappuccino"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "4"):
            drinkSpecial = "Espresso"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "5"):
            drinkSpecial = "Flat White"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "6"):
            drinkSpecial = "Latte"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "7"):
            drinkSpecial = "Macchiato"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "8"):
            drinkSpecial = "Mocha"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
    elif (coffee1 == "2"):
        print("You picked iced coffee.")
        hotIced = "Iced"
        coffee2 = input("(1) Americano \n(2) Brew \n(3) Cappuccino \n(4) Espresso Shot \n(5) Flat White \n(6) Latte \n(7) Macchiato \n(8) Mocha \n")
        if (coffee2 == "1"):
            drinkSpecial = "Americano"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "2"):
            drinkSpecial = "Brew"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "3"):
            drinkSpecial = "Cappuccino"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "4"):
            drinkSpecial = "Espresso Shot"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "5"):
            drinkSpecial = "Flat White"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "6"):
            drinkSpecial = "Latte"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "7"):
            drinkSpecial = "Macchiato"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
        elif (coffee2 == "8"):
            drinkSpecial = "Mocha"
            print("Here is your " + hotIced + " " + drinkType + " " + drinkSpecial + "! Have a nice day!")
elif (user2 == "2"):
    print("You picked tea.")
    drinkType = "Tea"
    tea1 = input("Would you like (1) hot or (2) iced tea? \n")
    if (tea1 == "1"):
        hotIced = "Hot"
        tea2 = input("(1) Chai \n(2) Black \n(3) Green \n(4) Herbal \n(5) White \n")
        if (tea2 == "1"):
            drinkSpecial = "Chai"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "2"):
            drinkSpecial = "Black"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "3"):
            drinkSpecial = "Green"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "4"):
            drinkSpecial = "Herbal"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "5"):
            drinkSpecial = "White"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
    elif (tea1 == "2"):
        hotIced = "Iced"
        tea2 = input("(1) Chai \n(2) Black \n(3) Green \n(4) Herbal \n(5) White \n")
        if (tea2 == "1"):
            drinkSpecial = "Chai"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "2"):
            drinkSpecial = "Black"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "3"):
            drinkSpecial = "Green"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "4"):
            drinkSpecial = "Herbal"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (tea2 == "5"):
            drinkSpecial = "White"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
elif (user2 == "3"):
    print("You picked frappuccino.")
    drinkType = "Frappuccino"
    frap1 = input("Would you like a (1) coffee or (2) creme frappuccino? \n")
    if (frap1 == "1"):
        hotIced = "Coffee"
        frap2 = input("(1) Caramel \n(2) Java Chip \n(3) Mocha \n(4) Caffe Vanilla \n(5) Espresso \n")
        if (frap2 == "1"):
            drinkSpecial = "Caramel"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "2"):
            drinkSpecial = "Java Chip"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "3"):
            drinkSpecial = "Mocha"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "4"):
            drinkSpecial = "Caffe Vanilla"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "5"):
            drinkSpecial = "Espresso"
            print ("Here is your " + hotIced + " " + drinkSpecial + " " + drinkType + "! Have a nice day!")
    elif (frap1 == "2"):
        hotIced = "Creme"
        frap2 = input("(1) Vanilla Bean \n(2) Double Chocolatey Chip \n(3) Matcha Green Tea \n(4) Cotton Candy \n(5) Chai \n")
        if (frap2 == "1"):
            drinkSpecial = "Vanilla Bean"
            print ("Here is your " + drinkSpecial + " " + hotIced + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "2"):
            drinkSpecial = "Double Chocolatey Chip"
            print ("Here is your " + drinkSpecial + " " + hotIced + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "3"):
            drinkSpecial = "Matcha Green Tea"
            print ("Here is your " + drinkSpecial + " " + hotIced + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "4"):
            drinkSpecial = "Cotton Candy"
            print ("Here is your " + drinkSpecial + " " + hotIced + " " + drinkType + "! Have a nice day!")
        elif (frap2 == "5"):
            drinkSpecial = "Chai"
            print ("Here is your " + drinkSpecial + " " + hotIced + " " + drinkType + "! Have a nice day!")
elif (user2 == "4"):
    print("You picked other.")
