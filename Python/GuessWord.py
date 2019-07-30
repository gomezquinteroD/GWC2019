import random

# A list of words that
potential_words = ["code", "sisterhood", "program", "empower", "team", "atom", "technology", "notebook", "marker"]

word = random.choice(potential_words)

# Use to test your code:
#print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word
for i in range(len(word)):
    current_word.append("_")

print (current_word)

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter or word: ")
	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if guess in word:
        if len(guess) == 1: #letter
            for g in range(len(word)):
                if guess == word[g]:
                    current_word[g] = guess
        elif guess == word:
            print ("You have guessed the word!")
            break

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

    print(current_word)
    if "_" in current_word:
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")
    else:
        print ("You have guessed the word!")
        break
