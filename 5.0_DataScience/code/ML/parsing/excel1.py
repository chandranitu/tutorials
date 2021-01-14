#pip install openpyxl
#python3

import os
import pandas as pd
import xlwt
import openpyxl
from openpyxl import Workbook
 
# Workbook is created
wb = Workbook()
type(wb)
ws=wb.active
type(ws)
ws.title='test'
# add_sheet is used to create sheet.
wb.sheet_properties.tabcolor="12345"
 


wb.save('/home/hadoop/J2EE_TRAINING/Python/code/serialization/sample1.xls')


