def chooseMedia():
    print ("Should we be an Instagram Star or a Twitter Star?")
    answer = input("Insta or Twitter? ")
    if (answer == "Insta"):
        print ("Instagram all the way!")
        InstaPath()
    elif (answer == "Twitter"):
        print ("Twitter is the way to go")
        TwitterPath()
    else:
        print ("That's not one of my choices")
        chooseMedia()

def InstaPath():
    print ("What should our insta handle be? ")
    username = input("@")
    username = "@" + username
    print ("My handle is " + username)


def TwitterPath():
    print ("What should our twitter handle be? ")
    username = input("@")



#------------------------------------Start

print ("Social media is so fun. I should try to be a social media star!")
answer = input("Should I be a star? (Y or N) \n")

if (answer == "Y"):
    print ("Yes let's do it!")
    chooseMedia()
elif (answer == "N"):
    print ("How bout I do anyway")
    chooseMedia()
else: print ("That's not yes or no..")
