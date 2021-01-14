import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

columns = "age sex bmi map tc ldl hdl tch ltg glu".split()  # Declare the columns names

# datasets="/home/hadoop/hadoop/hadoop_working/DataScience/code/sklearn/diabetic.txt"

diabetes = datasets.load_diabetes()  # Call the diabetes dataset from sklearn

df = pd.DataFrame(diabetes.data, columns=columns)  # load the dataset as a pandas data frame

y = diabetes.target  # define the target variable (dependent variable) as y

# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# fit a model
lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

predictions[0:5]

## The line / model
plt.scatter(y_test, predictions)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()

# Accuracy
print("Score:", model.score(X_test, y_test))
