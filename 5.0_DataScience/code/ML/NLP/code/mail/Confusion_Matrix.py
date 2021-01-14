
# coding: utf-8

# In[25]:

import pandas as pd
from sklearn.metrics import confusion_matrix
import distance
import numpy as np


# In[26]:
Manual_BRCA_1/
df = pd.read_csv("/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/7.NLP/code/mail/myraidmanual_confusion3.csv")


# In[31]:

df = df.applymap(str)


# In[23]:

df.columns


# In[33]:

df.describe()


# In[36]:

def matrix_cal(input_string1,input_string2):
	matrix = 'Notfnd'
	try:
		matrix = confusion_matrix(input_string1, input_string2)
	except:
		' '
	return matrix
	
def mainfunction(record):
	manual_status1 = record.manual_status1
	machine_status1 = record.machine_status1
	confusion_matrix = matrix_cal(manual_status1,machine_status1)
	return confusion_matrix
	
hive_df = sqlContext.sql('select * from checkt')
hive_df.registerTempTable("mDNA_Biomarker_ILS")
data_df = sqlContext.sql('select * from mDNA_Biomarker_ILS')
	
result 	= data_df.rdd.map(mainfunction)
	
0ms@ir@m

confusion_matrix(df['Manual_BRCA_1'], df['Machine_BRCA_1'])


# In[39]:

confusion_matrix(df['Manual_BRCA_2'], df['Machine_BRCA_2'])

