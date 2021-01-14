import pandas as pd
from sklearn import datasets1, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

columns = "age sex bmi map tc ldl hdl tch ltg glu".split()  # Declare the columns names

datasts = pd.read_csv("diabetic.txt")
print(type(datasts))
print(datasts.dtypes)
print(datasets.describe())  # all will be print
#datasets.describe()  # stats data retrieve
# datasets['age'].astype(str)

# rdd1=datasets.map(lambda x: (x[:55],x[55:85],x[85:115],x[115:125],x[125:150],x[150:175]))

datasets11 = pd.read_csv("file:///home/hadoop/hadoop/hadoop_working/DataScience/code/sklearn/diabetic.txt")
df = pd.DataFrame(datasets11, columns=columns)  # load the dataset11 as a pandas data frame
y = datasets11  # define the target variable (dependent variable) as y
# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
