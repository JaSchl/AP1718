import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 18


x, y = np.genfromtxt('wertee.txt', unpack=True)

def f(x):
    return (2.1609 * x)/((15.60 + x)**2)

#params, covariance_matrix = curve_fit(f, x, y)

#errors = np.sqrt(np.diag(covariance_matrix))

#a = ufloat(params[0], errors[0])
#b = ufloat(params[1], errors[1])

#print(a, b)
#matplotlib inline
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16


x_plot = np.linspace(0, 51)

plt.plot(x, y, 'k+', label="Werte")
plt.plot(x_plot, f(x_plot), 'r-', label='Theoriekurve', linewidth=3)
plt.xlabel('$R_a/\Omega$')
plt.ylabel('N/kW')
plt.legend(loc="best")
plt.savefig('plote.pdf')
