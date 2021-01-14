#python2

import os
import pandas as pd
import numpy as np
import xlwt
from xlwt import Workbook
 

##
var3 = '/home/hadoop/J2EE_TRAINING/Python/code/parsing/abc.xlsx'

m3=pd.ExcelFile(var3)
df3 = m3.parse('sheet1')

df3.head(5)   #top5

#Deleting column

del df3['NEWCOL']

#can use drop too dfd = df3.drop('NEWCOL', 1) 

writer = pd.ExcelWriter('/home/hadoop/J2EE_TRAINING/Python/code/parsing/abc.xlsx', engine='xlsxwriter')

df3.to_excel(writer)
writer.save()




