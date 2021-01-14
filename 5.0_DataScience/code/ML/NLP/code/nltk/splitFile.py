import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
import re

words = re.split(r'\W+', text)
print(words[:100])



