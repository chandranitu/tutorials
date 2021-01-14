import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
#Find #hashtags in line
#Create a keyvalue pair with {#hashtags, tweetline)
#Send tweetline in parallel to an API for sentiment score [1 for positive; 0 for neutral and -1 for -ve]
#Display a sentiment score chart on timeline vs #hashtag
#Also, display all the tweets with its sentiment and hashtag filter

#Import
from bs4 import BeautifulSoup 
import urllib.request 
from nltk.corpus import stopwords 
import nltk 


#hs="file:///home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/7.NLP/code/rategain/Tweets.txt"
hs="/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/7.NLP/code/rategain/Tweets.txt"

#print(sent_tokenize(hs))
#print(word_tokenize(hs))

with open (hs) as fin:tokens = word_tokenize(fin.read())
word_features = []
clean_tokens = tokens[:] 

freq = nltk.FreqDist(tokens)
for key,val in freq.items():  print (str(key) + ':' + str(val))

##use stop words to eliminate all words except #words
#sr = stopwords.words('english')

for token in tokens: 
  if token in stopwords.words('english'):clean_tokens.remove(token) 

freq = nltk.FreqDist(clean_tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))

freq.plot(20,cumulative=False)

## Rating based on  1 for positive; 0 for neutral and -1 for -ve


rating = 0
for row in word_features:
if i == row[0]:
print (i, row[1])
if row[1] == 'pos':
rating = rating + 1
elif row[1] == 'neg':
rating = rating - 1
print  (rating)

