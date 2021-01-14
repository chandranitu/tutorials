import pandas as pd
import numpy as np

df = pd.DataFrame()
print (df)

#DataFrame from Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)


data = [['chandra',10],['raj',12],['ram',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)
