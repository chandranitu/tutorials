# For Linux/OS X
#pip install -U pip setuptools
# For Windows
#python -m pip install -U pip setuptools

#Anaconda
#pip install XlsxWriter
#pip install xlrd
#python2

import os
import pandas as pd
import xlwt

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

# Change directory 
#os.chdir("D:\J2EE_TRAINING\Python\code\serialization")
os.chdir("/home/hadoop/J2EE_TRAINING/Python/code/serialization")

# List all files and directories in current directory
os.listdir('.')

#file = 'D:\J2EE_TRAINING\Python\code\serialization\test.xlsx'
var1 = '/home/hadoop/J2EE_TRAINING/Python/code/serialization/test.xlsx'
# Load spreadsheet
xl = pd.ExcelFile(var1)
print(xl.sheet_names)
df1 = xl.parse('ericsson')
#df = pd.read_csv("test.csv")

data = [[2,'eric1',10],[3,'eric2',12],[5,'ram',13]]
df = pd.DataFrame(data,columns=['id','name','Age'])


print (df)

#writer = pd.ExcelWriter('test1.xlsx')
writer = pd.ExcelWriter('test1.xlsx', engine='xlsxwriter')
df.to_excel(writer, 'a')

# Save the result 
writer.save()

