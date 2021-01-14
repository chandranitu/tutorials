import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

para = "What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid"

sentense = word_tokenize(para)
word_features = []

for i,j in nltk.pos_tag(sentense):
    if j in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:word_features.append(i)


