#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft,ifft
import numpy as np

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print y

yinv = ifft(y)
print yinv


time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 *np.random.randn(time_vec.size)
print sig.size
