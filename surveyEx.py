import json
#create an empty dictionary


#create a list of survey questions
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "Do you like this program?",
    "cats or dogs?"]
#create a list of keys related to the questions
keys = ["name", "age", "hometown", "like", "pet"]
#loop through the questions list and take user input
allanswers = []

anothersurvey = "yes"
while anothersurvey == "yes":
    answers = {}
    i = 0
    for q in survey:
        print(q)
        useri = input()
        answers[keys[i]] = useri
        i +=1
    allanswers.append(answers)
    anothersurvey = input("Submit another survey? (y or n):  ")

print(allanswers)
#attempt to read file
with open('surveyResp.json') as f:
    try:
         olddata = json.load(f)
    except ValueError:
         olddata = []
allanswers.extend(olddata)
f.close()
#write to file
f = open("surveyResp.json", "w")
json.dump(allanswers, f)
f.close()

#see if popularity is dog or cat
count = 0
catCount = 0
dogCount = 0
for u in allanswers:
    count +=1
    ans = u["pet"]
    if ans == "cats":
        catCount +=1
    else:
        dogCount +=1
if catCount > dogCount:
    print(str(catCount) + " out of " + str(count) + " are cat people!")
else:
    print(str(dogCount) + " out of " + str(count) + " are dog people!")
