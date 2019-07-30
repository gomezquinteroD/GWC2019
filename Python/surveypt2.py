import json

# Create a list of survey questions and a list of related keys that will be used when storing survey results.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)"]
keys = ["name", "age", "hometown", "DOB"]

#create a list to hold all user's answers
allAnswers = []

done = "no"
while done == "no":
    #create new dictionary for new user
    answers = {}
    print("Hi new user! Please answer the questions below! ")
    # Iterate over the list of survey questions and take in user responses.
    i = 0 #index
    for question in survey:
        response = input(survey[i] +":     ")
        answers[keys[i]] = response
        i += 1 #increase index by 1
    #add the dictionary of answers to our large answer list
    allAnswers.append(answers)
    done = input("Are you done collecting information? (yes or no):  ")

print("Here are all of the answers collected: ")
print(allAnswers)

# Reopen the file in write mode and write each entry in json format.
f = open("surveyResp.json", "r")
olddata = json.load(f)
allAnswers.extend(olddata)
f.close()

f = open("surveyResp.json", "w")
f.write('[\n')
index = 0
for t in allAnswers:
    if (index < len(allAnswers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
