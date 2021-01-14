import pandas as pd
import numpy as np

# From 3D ndarray
data = np.random.rand(2, 4, 5)
p = pd.Panel(data)
print(p)

# From dict of DataFrame Objects
data = {'Item1': pd.DataFrame(np.random.randn(4, 3)),
        'Item2': pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

# Empty panel
p = pd.Panel()
print(p)
