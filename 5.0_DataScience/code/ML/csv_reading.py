from tkinter.filedialog import Open
import pandas
import csv

path = '/home/hadoop/contribDB_1980.csv'

with open(path) as f:
    lis = [line.split() for line in f]        # create a list of lists
    for i, x in enumerate(lis):              #print the list items
        print ( "line{0} = {1}".format(i, x))





--------------------
import pandas
import csv
path = 'home/hadoop/contribDB_1980.csv'

with open(path, 'rt')as f:
    data = csv.reader(f)
    for row in data:
        print(row)
