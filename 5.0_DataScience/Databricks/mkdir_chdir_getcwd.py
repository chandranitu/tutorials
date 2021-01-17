#
#import os
#import glob
#os.getcwd()
#os.mkdir('/dbfs/mlflow/iris')
#os.chdir('/chandra')
# File name  
file = 'file1.txt'    
# File location  
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
# Path  
path = os.path.join(location, file)  
    
# Remove the file  
# 'file.txt'  
os.remove(path)  
