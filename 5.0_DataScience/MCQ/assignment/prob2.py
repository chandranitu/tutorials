Problem 2:-----

import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/chandrashekhar_kumar/Downloads/a_project/AI_ML/proj1/FAO.csv',encoding='ISO-8859-1')
#string array of cereals
#df=pd.read_csv('C:/Users/chandrashekhar_kumar/Downloads/a_project/AI_ML/proj1/FAO.csv',encoding='ISO-8859-1',usecols=['Item'], squeeze=True)
# sorting by first name 
df.sort_values("Item", inplace = True) 
df.drop_duplicates(subset='Item', keep='first', inplace=True)
arr = df['Item'].values
print("unique string array",arr)

# USA data
df1=pd.read_csv('C:/Users/chandrashekhar_kumar/Downloads/a_project/AI_ML/proj1/FAO.csv',encoding='ISO-8859-1')
df1 = df1.loc[df1['Area Abbreviation'] == 'USA' ]

strarr=['Wheat','Rice','Barley','Corn (Maize)','Rye','Oats','Millet','Sorghum','Other Cereals']
#shorthand
strarr1=[w[:2] for w in strarr]
#['Wh', 'Ri', 'Ba', 'Co', 'Ry', 'Oa', 'Mi', 'So', 'Ot']
