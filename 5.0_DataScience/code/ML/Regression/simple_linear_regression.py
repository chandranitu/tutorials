# Simple Linear Regression
#python3
# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import spatial

# Importing the dataset
dataset = pd.read_csv('/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/code/ML/Regression/Salary_Data.csv',encoding='ISO-8859-1')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split  #depricated

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
"""plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()"""

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_test), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Predicting a new result
#Scikit does not work with scalars (just one single value). It expects a shape (m×n) where m is the number of features and n is the number of observations, both are 1 in this case.
Y_pred = regressor.predict(np.array([8.5]).reshape(1, 1))
