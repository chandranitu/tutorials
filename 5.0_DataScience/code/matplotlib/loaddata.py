#Plotting salary data

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('/home/hadoop/hadoop/hadoop_working/DataScience/code/matplotlib/Salary_Data.csv',unpack=True,delimiter = ',')

plt.plot(x,y)

plt.title('CNS Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
