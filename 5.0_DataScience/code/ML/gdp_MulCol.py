# Multiple Linear Regression

#python3

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
from numpy import reshape

#data is in different columns
dataset = pd.read_csv('/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/MLcode/2.gdp/gdp_MulColmns.csv')
dataset['years'], dataset['gdp'] = zip(*dataset['years\tgdp'].map(lambda x: x.split('\t')))

X = dataset.iloc[:,1:2].values.astype(float)
y = dataset.iloc[:,2:3].values.astype(float)


plt.plot(X,y,color='green',marker='o',linestyle='solid')
#add a title
plt.title("Nominal GDP")
#add a label to	the y-axis

plt.ylabel("Billions of $")
plt.show()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)


# Fitting Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


# Predicting the Test set results
y_pred = regressor.predict(X_test)

y_pred = regressor.predict(2012)


##
# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, y_pred, color = 'blue')
plt.scatter(X_train,y_train, color = "green")
plt.title('Years vs gdp (Test set)')
plt.xlabel('Years ')
plt.ylabel('GDP')
plt.show()
