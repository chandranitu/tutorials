
#python3

from matplotlib import pyplot as plt
from matplotlib import style 
import pandas as pd
import xlwt
import openpyxl

# Change directory 
#os.chdir("D:\J2EE_TRAINING\Python\code\serialization")
os.chdir("/home/hadoop/J2EE_TRAINING/Python/code/parsing")

# List all files and directories in current directory
os.listdir('.')
wb = Workbook()

data = [[2,'eric1',10],[3,'eric2',12],[5,'ram',13]]
df = pd.DataFrame(data,columns=['id','name','Age'])

x=df['name']
y=df['Age']

plt.title('CNS Info')
plt.ylabel('Age')
plt.xlabel('Name')
#plt.show()
#print (df)
plt.savefig("myplot.png", dpi = 150)
img = openpyxl.drawing.Image('myplot.png')

wb.save('/home/hadoop/J2EE_TRAINING/Python/code/serialization/output.xlsx')
