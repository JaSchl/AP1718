import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (10, 20)
plt.rcParams['font.size'] = 18


x, y = np.genfromtxt('Wertehysterese2.txt', unpack=True)
#def f(x, a, b):
    #return a * x + b

#params, covariance_matrix = curve_fit(f, x, y)

#errors = np.sqrt(np.diag(covariance_matrix))

#a = ufloat(params[0], errors[0])
#b = ufloat(params[1], errors[1])

#print(a, b)
#matplotlib inline
plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams['font.size'] = 15


x_plot = np.linspace(0, 20)

plt.plot(x, y, 'k.', label="werte")
#plt.plot(x_plot, f(x_plot, *params), 'r-', label='linearer Fit', linewidth=3)
plt.legend(loc="best")

plt.savefig('plothys2.pdf')
