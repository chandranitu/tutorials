#Our function will be this — f(x) = x³ — 5x² + 7

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#creating the function and plotting it 

function = lambda x: (x ** 3)-(3 *(x ** 2))+7

#Get 1000 evenly spaced numbers between -1 and 3 (arbitratil chosen to ensure steep curve)
x = np.linspace(-1,3,500)

#Plot the curve
plt.plot(x, function(x))
plt.show()
#----------------

fn=lambda x,y: -((cosx)**2+(cosy)**2)**2
x = np.linspace(-1,3,500)
y = np.linspace(-1,5,200)

#Plot the curve
plt.plot(x,y)
plt.show()
#----------------
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()

#-------------
import matplotlib.pyplot as plt # For ploting
import numpy as np # to work with numerical data efficiently

fs = 100 # sample rate 
f = 2 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [ np.sin(2*np.pi*f * (i/fs)) for i in x]

#this instruction can only be used with IPython Notbook. 
# showing the exact location of the smaples
plt.stem(x,y, 'r', )
plt.plot(x,y)
