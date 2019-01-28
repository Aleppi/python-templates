import matplotlib
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import lmfit as lm
matplotlib.style = 'ggplot'
matplotlib.rc('text', usetex = True)
matplotlib.rc('font', **{'family' : 'sans-serif', 'size' : 12})
matplotlib.rc('grid', linestyle=':')
pltParams = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
plt.rcParams.update(pltParams)

csv = np.genfromtxt('<++>.csv', delimiter=',')
x = <++>[:,0]
y = <++>[:,1]

plt.plot(x, y, marker='.', linestyle='none', color='b', label='<++>')

plt.axis(<++>)
plt.grid(True)
plt.xlabel(r"$<++>$")
plt.ylabel(r"$<++>$")
plt.legend(loc='best')
plt.savefig('<++>.pdf', bbox_inches='tight')
plt.show()
