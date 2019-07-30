#create a dictionary
answers = {}

# Create a list of survey questions and a list of related keys that will be used when storing survey results.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)"]
keys = ["name", "age", "hometown", "DOB"]
# Iterate over the list of survey questions and take in user responses.
i = 0 #index
for question in survey:
    response = input(survey[i] +":     ")
    answers[keys[i]] = response
    i += 1 #increase index by 1

print(answers)
