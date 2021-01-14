import pandas as pd
import numpy as np

s = pd.Series()
print (s)

#Create a Series from ndarray

data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data)
print (s)


data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data,index=[100,101,102,103,104,105])
print (s)
