#python3

import os
import pandas as pd
import xlwt
from xlwt import Workbook
from matplotlib import pyplot as plt
from matplotlib import style
 

##
var3 = '/home/hadoop/J2EE_TRAINING/Python/code/parsing/test.xlsx'

#idx='UCell Id'
m3=pd.ExcelFile(var3)

df3 = m3.parse('ericsson')
print(df3.head(5))
x=df3['name']
y=df3['age']

plt.title('CNS Info')
plt.ylabel('Age')
plt.xlabel('Name')
plt.show()





