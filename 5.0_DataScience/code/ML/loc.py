# loc indexer for Pandas Dataframe is used for col-location based indexing / selection by position.
import pandas as pd

df = pd.read_csv('/home/hadoop/1.0tutorials/hadoop_working/5.0_DataScience/5.MachineLearning/1.DataPreprocessing/Data.csv')

# Create the index 
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5','Row_6', 'Row_7', 'Row_8', 'Row_9', 'Row_10'] 

# Set the index 
df.index = index_ 

# return the value 
result = df.loc['Row_2', 'Age'] 
  
# Print the result 
print(result) 







--------------------------------
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany  40.0      NaN       Yes
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes

