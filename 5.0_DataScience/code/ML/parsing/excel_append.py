#python2

import os
import pandas as pd
import xlwt
from xlwt import Workbook
 
var1 = '/home/hadoop/J2EE_TRAINING/Python/code/serialization/m1.xlsx'
var2 = '/home/hadoop/J2EE_TRAINING/Python/code/serialization/m2.xlsx'
# Load spreadsheet
m1 = pd.ExcelFile(var1)
m2 = pd.ExcelFile(var2)
#print(xl.sheet_names)
df1 = m1.parse('ericsson')
df2 = m2.parse('ericsson')

#Append

df=df1.append(df2)

writer = pd.ExcelWriter('/home/hadoop/J2EE_TRAINING/Python/code/serialization/test121.xlsx', engine='xlsxwriter')
df.to_excel(writer, 'sheet1')

#copy excelsheet

# Save the result 
writer.save()






