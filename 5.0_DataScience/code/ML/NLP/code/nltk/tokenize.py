import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
print (html)


from bs4 import BeautifulSoup
import urllib.request 
response = urllib.request.urlopen('http://php.net/') 
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
print (text)




from bs4 import BeautifulSoup 
import urllib.request 
response = urllib.request.urlopen('http://php.net/') 
html = response.read() 
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
print (tokens)
