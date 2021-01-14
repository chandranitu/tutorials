import os
import pandas as pd
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet1')

sheet1.write(1, 0, 'ISBT')
sheet1.write(2, 0, 'Airport')
sheet1.write(3, 0, 'Railway')
sheet1.write(4, 0, 'Bus stand')
sheet1.write(5, 0, 'CLOCK TOWER')

wb.save('/home/hadoop/J2EE_TRAINING/Python/code/serialization/sample.xls')