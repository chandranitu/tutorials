#!/usr/bin/python
#python3

import pandas as pd

def cols(self):
    """list of column names containing the string 'cns'
    """
    return [x for x in self.columns if 'cns' in x]

pd.DataFrame.cols = cols # monkey-patch the DataFrame class
df = pd.DataFrame([list(range(4))], columns=["A","cns","football","delhi"])
df.cols()
del pd.DataFrame.cols # remove the new method
