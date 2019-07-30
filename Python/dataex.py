import json
from textblob import TextBlob
import matplotlib.pyplot as plt


#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polar = []
subj = []

bigtweet = ""
for tweet in tweetData:
    text = tweet["text"]
    tb = TextBlob(text)

    pol = tb.polarity
    polar.append(pol)

    sub = tb.subjectivity
    subj.append(sub)

    bigtweet += text

bigblob = TextBlob(bigtweet)
filterd = {}

wordsList = bigblob.words
for word in wordsList:
    #filters here
    if len(word) < 2:
        continue

    filterd[word] = bigblob.word_counts[word]
#create the word cloud
