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

