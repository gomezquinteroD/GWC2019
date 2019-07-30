import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []

for tweet in tweetData:
    text = tweet['text']
    tb = TextBlob(text)
    polar = tb.polarity
    subj = tb.subjectivity

plt.hist(polarity, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])

#label the x axis
plt.xlabel('Polarities')
#label the y axis
plt.ylabel('Number of Tweets')
#title the graph
plt.title('Histogram of Tweet Polarity')
#ranges for x axis (-1.1, 1.1) & y axis (0,100)
plt.axis([-1.1, 1.1, 0, 100])
#show the grid
plt.grid(True)
#show the whole histogram
plt.show()
