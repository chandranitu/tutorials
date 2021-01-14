import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

#Feature extraction
#Based on the dataset, we prepare our feature. The feature we will use is the last letter of a name:
 
def gender_features(word): 
    return {'last_letter': word[-1]} 
 
# Load data and training 
names = ([(name, 'male') for name in names.words('male.txt')] + 
	 [(name, 'female') for name in names.words('female.txt')])
 
featuresets = [(gender_features(n), g) for (n,g) in names] 
train_set = featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set) 
 
# Predict
print(classifier.classify(gender_features('chandra')))



#For Python 2, use raw_input.



