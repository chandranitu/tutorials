# F1 Score

#python3

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

# FORMULA
# F1 = 2 * (precision * recall) / (precision + recall)

# load dataset
path = '/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/code/ML/1.sample/titanic.csv'
data = pd.read_csv(path,sep="\\", names=['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'],encoding='ISO-8859-1')
#X = pd.DataFrame(data.strip())
X = pd.DataFrame(data)
X.head(1)

#index_col=0
#'PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'

# only store numeric data in features
X = X._get_numeric_data()
X.head(1)

# create response vector y
y = X.Survived
y.head(3)

# delete 'Survived', the response vector (Series)
X.drop('Survived', axis=1, inplace=True)

# we drop age for the sake of this example because it contains NaN in some examples
X.drop('Age', axis=1, inplace=True)

# check delete
X.head()

# imports for classifiers and metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score

# train/test split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Decision Tree Classifier----------
# instantiate
dtc = DecisionTreeClassifier()

# fit
dtc.fit(X_train, y_train)

# predict
y_pred = dtc.predict(X_test)

# f1 score
score = f1_score(y_pred, y_test)

# print
print("Decision Tree F1 score: {:.2f}".format(score))

# Gaussian Naive Bayes

# instantiate
gnb = GaussianNB()

# fit
gnb.fit(X_train, y_train)

# predict
y_pred_2 = gnb.predict(X_test)

# f1 score
score_2 = f1_score(y_pred_2, y_test)

# print
print("GaussianNB F1 score: {: .2f}".format(score_2))




