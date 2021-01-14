
Problem 3:---

import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/chandrashekhar_kumar/Downloads/a_project/AI_ML/proj1/FAO.csv',encoding='ISO-8859-1')
import os
os.getcwd()
#os.chdir('Downloads/a_project/AI_ML/proj1')
import csv
inputs = ["FAO.csv", "groupData.csv"]  # etc

# First determine the field names from the top line of each input file
# Comment 1 below
fieldnames = []
for filename in inputs:
  with open(filename, "r", newline="") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for h in headers:
      if h not in fieldnames:
        fieldnames.append(h)

# Then copy the data
with open("out.csv", "w", newline="") as f_out:   # Comment 2 below
  writer = csv.DictWriter(f_out, fieldnames=fieldnames)
  for filename in inputs:
    with open(filename, "r", newline="") as f_in:
      reader = csv.DictReader(f_in)  # Uses the field names in this file
      for line in reader:
        # Comment 3 below
        writer.writerow(line)


