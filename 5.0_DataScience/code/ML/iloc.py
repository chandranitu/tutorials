# iloc indexer for Pandas Dataframe is used for integer-location based indexing / selection by position.
import pandas as pd

data = pd.read_csv('/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/5.MachineLearning/1.DataPreprocessing/Data.csv')

## Rows:
data.iloc[0] # first row of data frame
data.iloc[1] #vertical
data.iloc[:1] #horizontal
data.iloc[:-1] #till last row of data fram

# Columns:
data.iloc[:,0] # first column of data frame 
data.iloc[:,1] # second column of data frame
data.iloc[:,-1] # till last column of data frame 

