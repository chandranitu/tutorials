# Reading text file and saving into CSV file

import csv
import pandas
txt_file = r"D:\project\datascience\mobile\code\test.txt"
csv_file = r"D:\project\datascience\mobile\code\mobile1.csv"

df = pandas.read_csv(txt_file,delimiter=",")
df.to_csv(csv_file, encoding='utf-8', index=False)


------------------------ 
with open(txt_file, "r") as in_text:
    in_reader = csv.reader(in_text, delimiter = ',', lineterminator='\n',)
with open(csv_file, "w") as out_csv:
     out_writer = csv.writer(out_csv, 'w')
		for row in in_reader:
		out_writer.writerow(row)

#with open(r"D:\project\datascience\mobile\code\test.txt","rb") as f1: 

csv_file="D:\project\datascience\mobile\code\mobile1.csv"

in_txt = csv.reader(open(r"D:\project\datascience\mobile\code\test.txt","rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))
#    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
     for line in f1:       
       print(f1.read())
		
		
import csv
    with open ('test_data.txt', 'rb') as f:

    for line in f:
        dict_file = eval(f.read())
        time = (dict_file['t'])    # print (time) result [1494257340]
        open_price = (dict_file['o'])    # print (open_price) result [206.7]
        high = (dict_file['h'])    # print (high) result [209.3]
        low = (dict_file['l'])    # print (low) result [204.50002]
        close = (dict_file['c'])    # print (close) result [204.90001]
        volume = (dict_file['v'])    # print (volume) result [49700650]

        print (time, open_price, high, low, close, value)