import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)

# DataFrame from Lists
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)

data = [['chandra', 10], ['raj', 12], ['ram', 13]]
df1 = pd.DataFrame(data, columns=['Name', 'Age'])
print(df1)
# ---------------

df2 = pd.DataFrame({"Name": ["Alice", "Bob", "Mallory", "Mallory", "Bob", "Mallory"],
                    "City": ["Seattle", "Louis", "Portland", "Seattle", "Seattle", "Portland"]})
print(df2)

g1 = df2.groupby(["Name", "City"]).count()
print(g1)
