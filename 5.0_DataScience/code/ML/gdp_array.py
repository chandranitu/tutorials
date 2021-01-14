# Multiple Linear Regression

#python3

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
from numpy import reshape

#dataset = pd.read_csv('/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/MLcode/2.gdp/gdp.csv')
#X = dataset.iloc[:, :-1].values
#y = dataset.iloc[:1].values

#x,y = np.loadtxt('/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/MLcode/2.gdp/gdp.csv', delimiter=",", unpack=True)   #values of x,y in one column


years=array([1950,1960,1970,1980,1990,2000,2010])
years=years.reshape(years.shape[0],1) #reshaping  in 1D to 2D

gdp=array([300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3])

plt.plot(years,gdp,color='green',marker='o',linestyle='solid')

#add a title
plt.title("Nominal GDP")
#add a label to	the y-axis

plt.ylabel("Billions of $")
plt.show()

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(years,gdp, test_size = 0.2, random_state = 0)


# Fitting Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


# Predicting the Test set results
y_pred = regressor.predict(X_test)

#predicting 2018 value
data=array([2018,2019,2020])
data=data.reshape(data.shape[0],1)
a=regressor.predict(data)

a=regressor.predict(2018)


##
# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_test), color = 'red')
plt.title('Years vs gdp (Test set)')
plt.xlabel('Years ')
plt.ylabel('GDP')
plt.show()
