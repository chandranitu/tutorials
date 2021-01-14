# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import impute
from sklearn.impute import SimpleImputer


# Importing the dataset
dataset = pd.read_csv('/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/5.MachineLearning/1.DataPreprocessing/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
#from sklearn.preprocessing import Imputer  #depricated
#sklearn.impute.SimpleImputer(missing_values=nan, strategy='mean', fill_value=None, verbose=0, copy=True, add_indicator=False)

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
