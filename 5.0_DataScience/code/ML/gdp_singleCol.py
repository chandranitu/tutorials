# Multiple Linear Regression

#python3

import matplotlib.pyplot as plt
# Importing the libraries
import pandas as pd
from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv('/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/MLcode/2.gdp/gdp_SingleColmns.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#add a title
plt.title("Nominal GDP")
#add a label to	the y-axis

plt.ylabel("Billions of $")
plt.show()

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(years,gdp, test_size = 0.2, random_state = 0)


# Fitting Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)


# Predicting the Test set results
y_pred = regressor.predict(X_test)


##
# Visualising the Test set results
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_test), color = 'blue')
plt.title('Years vs gdp (Test set)')
plt.xlabel('Years ')
plt.ylabel('GDP')
plt.show()


seed = 7
scoring = 'accuracy'

#Logistic Regression (LR)
#Linear Discriminant Analysis (LDA)
#K-Nearest Neighbors (KNN).
#Classification and Regression Trees (CART).
#Gaussian Naive Bayes (NB).
#Support Vector Machines (SVM).

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=4, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
