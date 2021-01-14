# For Linux/OS X
#pip install -U pip setuptools
# For Windows
#python -m pip install -U pip setuptools

#Anaconda
#pip install XlsxWriter
#pip install xlrd
#pip install xlwt
#python2

import os
import pandas as pd
import xlwt
from xlwt import Workbook
 
# Workbook is created
wb = Workbook()
 
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('eric')

# (1-row  0 -column)
sheet1.write(1, 0,'NAME')
sheet1.write(1, 1,'AGE')
sheet1.write(2, 0, 'ISBT')
sheet1.write(3, 0, 'Airport')
sheet1.write(4, 0, 'Railway')
sheet1.write(5, 0, 'Bus stand')
sheet1.write(6, 0, 'CLOCK TOWER')
sheet1.write(6, 1,'test1123')

wb.save('/home/hadoop/J2EE_TRAINING/Python/code/serialization/sample.xls')


