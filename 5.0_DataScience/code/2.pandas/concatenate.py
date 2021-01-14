import pandas as pd
import numpy as np

df = pd.DataFrame()
print (df)

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
      		    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7']},index=[4, 5, 6, 7])
   

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},index=[8, 9, 10, 11])
   

frames = [df1, df2, df3]
pd.concat(frames)


pd.concat(frames, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)

result = pd.concat(frames, keys=['x', 'y', 'z'])
print result

result.loc['y']

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                      'D': ['D2', 'D3', 'D6', 'D7'],
                       'F': ['F2', 'F3', 'F6', 'F7']},
                       index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1, sort=False)

print result

result = pd.concat([df1, df4], axis=1, join='inner')
