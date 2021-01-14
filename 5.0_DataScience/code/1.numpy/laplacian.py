import numpy as np
from scipy.stats import laplace
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------------
# Define the distribution parameters to be plotted
delta_values = [0.5, 1.0, 2.0]
linestyles = ['-', '--', ':']
mu = 0
x = np.linspace(-10, 10, 1000)

#------------------------------------------------------------
# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for delta, ls in zip(delta_values, linestyles):
    dist = laplace(mu, delta)

    plt.plot(x, dist.pdf(x), ls=ls, c='black',
             label=r'$\mu=%i,\ \Delta=%.1f$' % (mu, delta))

plt.xlim(-6, 6)
plt.ylim(0, 1.0)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu,\Delta)$')
plt.title('Laplace Distribution')

plt.legend()
plt.show()
