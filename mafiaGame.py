from random import *

classN = ["Aadya", "Adriana", "Annie", "Brianna", "Catherine", "Gabrielle",
    "Jade", "Jennifer", "Jolina", "Joyce", "Kelsey", "Maggie", "Maria", "Megan",
    "Natalie", "Ruth", "Saira", "Sam", "Sana", "Taitu"]
absent = 'y'

while absent == "y":
    absent = input("Anyone absent? Y or N:  ")
    if absent == "n":
        break
    name = input("Enter absentee name:  ")
    classN.remove(name)

print("Current Class & length: ")
print(classN)
print(len(classN))

print("--------------------")
print("Welcome to Mafia")
