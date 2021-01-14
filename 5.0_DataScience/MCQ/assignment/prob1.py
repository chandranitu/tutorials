Problem 1:-----

import pandas as pd
import numpy as np
df=pd.read_csv('/home/hadoop/data/FAO.csv',encoding='ISO-8859-1')
#df=pd.read_csv('ml-100k/FAO.csv', sep='|', names=m_cols , encoding='latin-1')
#print(df.describe())
df1 = df.loc[df['Area Abbreviation'] == 'USA' ]
df2=df1.drop(['Area Code','Area','Item Code','Element Code','latitude','longitude','Element','Unit','Area Abbreviation'],axis=1)

X=df2[list(df2.columns)[1:63]]   #Y1961 Y1962 Y1963 Y1964..2013
Y=df2[list(df2.columns)[0]]          #Item   #Target state

X = pd.get_dummies(X) 
Y = pd.get_dummies(Y) 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
xTrain,xTest,yTrain,yTest=train_test_split(X,Y,random_state=42)
reg=LinearRegression()
reg.fit(xTrain,yTrain)
print(list(reg.predict(xTest))[:1])
print("Accuracy Score:",reg.score(xTest,yTest))
