import pandas as pd
import numpy as np


data = [[1,'chandra',10],[2,'raj',12],[3,'ram',13]]
df = pd.DataFrame(data,columns=['id','name','mobile'])
print (df)
---------

df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
columns=['a', 'b', 'c', 'd', 'e'])




