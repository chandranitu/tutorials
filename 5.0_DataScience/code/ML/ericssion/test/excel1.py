import os
import pandas as pd


# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

#file = 'D:\J2EE_TRAINING\Python\code\serialization\test.xlsx'
file = '/home/hadoop/J2EE_TRAINING/Python/code/serialization/test.xlsx'

xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('ericsson')




# Save the result
writer.save()
