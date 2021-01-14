# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/5.MachineLearning/1.DataPreprocessing/Data.csv')
X = dataset.iloc[:, :-1].values   # iloc indexer for Pandas Dataframe is used for integer-location based indexing / selection by position.
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split   #depricated

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
