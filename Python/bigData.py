import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#create a list for polarity & subjectivity
polarity = []
subj= []
bigT = ""

#turn the tweet data into a string for processing
for t in tweetData:
    plainT = t["text"]
    tweetb = TextBlob(t["text"])
    polarity.append(tweetb.polarity)
    subj.append(tweetb.subjectivity)
    bigT += plainT

#get the average polarity & subjectivity
sump = 0.0
sums = 0.0
total = 0
for p in polarity:
    sump += p
    total +=1
for s in subj:
    sums += p

sump = sump/total
sums = sums/total
#print
print(round(sump, 4))
print(round(sums,4))

#Create the Graph
#pls.hist(list of data, bins=[bar_condition1, bar_condition 2,...])
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

#Create WordCloud
bigblob = TextBlob(bigT)
tweetSearch = "automation"
#Filter Words
wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", tweetSearch, "they", "twitter"]
filteredDictionary = dict()

for word in bigblob.words:
	#skip tiny words
	if len(word) < 2:
		continue
	#skip words with random characters or numbers
	if not word.isalpha():
		continue
	#skip words in our filter
	if word.lower() in wordsToFilter:
		continue
	#don't want lower case words smaller than 5 letters
	if len(word) < 5 and word.upper() != word:
		continue;

	#Try lower case only, try with upper case!
    #word = the word, word_counts = # of times it is present in string
    #{"apple" : 3}
	filteredDictionary[word.lower()] = bigblob.word_counts[word.lower()]

#Create the word cloud
wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
