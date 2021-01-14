#pip install lxml
#pip3 install lxml
#sudo pip install six=1.10.0

#Tokenize Text Using Pure Python

import urllib.request
from bs4 import BeautifulSoup
import urllib.request 
import html5lib
import nltk 
from nltk.corpus import stopwords

#response = urllib.request.urlopen('https://www.google.co.in/')
response = urllib.request.urlopen('http://php.net/')

html = response.read()

#soup = BeautifulSoup(html,"google")
#soup = BeautifulSoup(html, "html5lib")

#soup = BeautifulSoup(html, "lxml")
soup = BeautifulSoup(html, features="xml")

text = soup.get_text(strip=True)
print (text)
tokens = [t for t in text.split()] 
print (tokens)

freq = nltk.FreqDist(tokens)
for key,val in freq.items():  print (str(key) + ':' + str(val))

#Remove Stop Words Using NLTK

stopwords.words('english')
