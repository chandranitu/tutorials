#python2

import os
import pandas as pd
import numpy as np
import xlwt
from xlwt import Workbook
 

##
var3 = '/home/hadoop/J2EE_TRAINING/Python/code/parsing/abc.xlsx'

#idx='UCell Id'
m3=pd.ExcelFile(var3)

df3 = m3.parse('Cell')
#df3['Ratio'] = df3['ReqCsSucc']/df3['Speech CSS Failed']

df3.head(5)   #top5
sLength = len(df3['ReqCsSucc'])

#Adding new column

df3['NEWCOL'] = pd.Series(np.random.randn(sLength),index=df3.index) #filling random number in new column 'NEWCOL'
writer = pd.ExcelWriter('/home/hadoop/J2EE_TRAINING/Python/code/parsing/abc.xlsx', engine='xlsxwriter')

df3.to_excel(writer)
writer.save()




