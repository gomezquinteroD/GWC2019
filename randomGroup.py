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


numG = input("Number of groups? 4 or 5:  ")
numG = int(numG)
group = []
for k in range(numG):
    if numG == 4:
        total = 5
    else:
        total = 4
    group = []
    for m in range(total):
        sm = len(classN) -1
        if sm == 1:
            sm +=1
        i = randint(0, sm)
        if i == len(classN):
            i -= 1
        group.append(classN[i])
        #print("added..." + classN[i])
        classN.remove(classN[i])

    print("This group is: ")
    print(group)
