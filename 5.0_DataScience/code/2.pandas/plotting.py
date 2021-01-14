
#sudo apt-get install python3-tk

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',periods=10), columns=list('ABCD'))

df.plot()
plt.show()

#bar plot
df.plot.bar()
plt.show()
