#create a list of survey questions
questions = ["what is your name?", "favorite animal?", "tea, coffee, or neither?",
    "Orange or Blue?", "What donut did you have today?"]
#create a list of related keys
keys = ["name", "animal", "drink", "color", "donut"]

#create a list to hold ALL user responses
allUsers = []

#set a condition for the while loop
done = "no"
while done == "no":
    #create an empty dictionary
    answers = {}
    #loop through your list of survey questions and take user input for responses
    index = 0
    for q in questions:
        ans = input(q)
        answers[keys[index]] = ans
        index +=1
    #after all questions asked, add the dictionary to the grand list
    allUsers.append(answers)
    #if done == yes, while loop stops
    done = input("Are you finished collecting information? (yes or no): ")
#print your user list
print(allUsers)
