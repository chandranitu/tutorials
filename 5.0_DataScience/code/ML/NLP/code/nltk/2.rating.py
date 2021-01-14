import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
import csv


rating = 0

for i in word_features:with open('/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/7.NLP/code/nltk/words.txt','rt') as f:
reader = csv.reader(f, delimiter=',')
for row in reader:
if i == row[0]:
print (i, row[1])
if row[1] == 'pos':
rating = rating + 1
elif row[1] == 'neg':
rating = rating - 1
print  (rating)
