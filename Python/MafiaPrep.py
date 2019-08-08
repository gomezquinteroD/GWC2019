from random import *
import os
names = ["Aadya", "Adriana", "Annie", "Brianna", "Catherine", "Gabrielle",
    "Jade", "Jennifer", "Jolina", "Joyce", "Kelsey", "Maggie", "Maria", "Megan",
    "Natalie", "Ruth", "Saira", "Sam", "Sana", "Taitu"]

absent = []

mafia = []
nurses = []
sheriffs = []

print("Let's Play Mafia!")
absentQ = input("Is anyone absent today? Y or N ")
if absentQ == 'Y':
    #add absent people
    absentQtwo = "Y"
    while absentQtwo == 'Y':
        absentee = input("Who is absent? ")
        absent.append(absentee)
        names.remove(absentee)
        print("Students absent: ")
        print(absent)
        absentQtwo = input("Anyone else? Y or N ")
        if absentQtwo == 'N':
            break

    #continue
print("Roles")
mafianum = input("How many Mafia players? ")
nursesnum = input("How many Nurse players? ")
shernum = input("How many Sheriff players? ")
mafianum = int(mafianum)
nursesnum = int(nursesnum)
shernum = int(shernum)

#MAFIA
for x in range(mafianum):
    newmaf = names[randint(0,len(names)-1)]
    mafia.append(newmaf)
    names.remove(newmaf)
print("Mafia crew is: ")
print(mafia)

#NURSES
for x in range(nursesnum):
    newnurse = names[randint(0,len(names)-1)]
    nurses.append(newnurse)
    names.remove(newnurse)
print("Nurse crew is: ")
print(nurses)

#SHERIFFS
for x in range(shernum):
    newsher = names[randint(0,len(names)-1)]
    sheriffs.append(newsher)
    names.remove(newsher)
print("Sheriff crew is: ")
print(sheriffs)

print("The game can now begin!")
goOn = input("Press enter to continue")
if goOn == '':
    os.system('cls')
game = True
targets = []
saved = []
day = 1
while game == True:
    print("Welcome to Day ", day)
    hanging = input("Are we lynching someone today? Y or N ")
    if hanging == 'Y':
        #proceed to hanging
        print("Who shall be hung today? ")
    #NIGHT MODE
    #Mafia
    elif hanging == 'N':
        os.system('cls')

    print("---START NIGHT MODE---")
    print("Mafia's turn: ")
    targetnum = input("How many targets tonight? ")
    targetnum = int(targetnum)
    for x in range(targetnum):
        target = input("Who is your target? ")
        targets.append(target)
    os.system('cls')
    print("Thank You Mafia\n")
    #NURSES
    print("Nurses' turn: ")
    savenum = input("How many people are being saved? ")
    savenum = int(savenum)
    for x in range(savenum):
        savedperson = input("Who will you save? ")
        saved.append(savedperson)
        if savedperson in targets:
            targets.remove(savedperson)
            print("** You saved a person! **")
    print("Thank you nurses\n")
    #Sheriffs
    print("Sheriffs' turn: ")
    investnum = input("How many people will be investigated? ")
    investnum = int(investnum)
    for x in range(investnum):
        invest = input("Who will you investigate? ")
        if invest in mafia:
            print("Mafia spotted!")
        else:
            print("All clear.")
    print("Thank you Sheriffs\n")
    print("---END NIGHT MODE---")
    print("The casualties are: ")
    print(targets)
    print("\n")
    print("The lucky souls are: ")
    print(saved)
    print("\n")
    cont = input("Continue? Y or N ")
    if cont == 'N':
        game = False
    day += 1
print("Thanks for playing Mafia!")
