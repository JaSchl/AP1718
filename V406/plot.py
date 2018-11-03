import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams['font.size'] = 15
plt.rcParams['lines.linewidth'] = 3


A, I = np.genfromtxt('mess75.txt', unpack=True)
I = I-5 #Abzug des dunkestroms
l = 633
A = A*10**3
A = A - 20000
L = 99.05 * 10**7

def f(x, A0, b, x0):
    return A0**2 * b**2* (l/(np.pi*b*np.sin((x-x0)/L)))**2*(np.sin(np.pi* b*np.sin((x-x0)/L)/l))**2

params, covariance_matrix = curve_fit(f, A, I, p0=[np.max(I), 0.00000015, 0.1])

errors = np.sqrt(np.diag(covariance_matrix))

print(' Parameter des Fits:')
print('         A0 =', params[0], '+/-', errors[0])
print('         b =', params[1], '+/-', errors[1])
print('         x0 =', params[2], '+/-', errors[2])
#matplotlib inline

x_plot = np.linspace(-12000, 16000)
plt.grid()
plt.plot(A, I, 'b+')

plt.plot(x_plot, f(x_plot, *params), 'r-', label='linearer Fit', linewidth=3)
plt.legend(loc="best")
plt.ylabel('$Strom/nA$')
plt.xlabel(r'$Abstand/\mu m}$')
plt.savefig('plot.pdf')
