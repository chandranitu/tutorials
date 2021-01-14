# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import impute
#from sklearn.preprocessing import Imputer   #depricated
from sklearn.impute import SimpleImputer

# Importing the dataset
dataset = pd.read_csv('/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/5.MachineLearning/1.DataPreprocessing/Data.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# missing data
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Encoding categorical data
# Encoding the Independent Variable

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
x[:, 0] = labelencoder_X.fit_transform(x[:, 0])
#onehotencoder = OneHotEncoder(categorical_features = [0])
#x= onehotencoder.fit_transform(x).toarray()

transformer = ColumnTransformer(
    transformers=[
        ("categorical_features", # Just a name
         OneHotEncoder(),        # The transformer class
         [0]                     # The column(s) to be applied on.
         )
    ],
    remainder='passthrough' # donot apply anything to the remaining columns
)
x = transformer.fit_transform(x.tolist())


# Encoding the Dependent Variable

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
