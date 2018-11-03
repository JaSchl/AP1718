import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 18

U, N = np.genfromtxt('1.txt', unpack=True)
N = N/60
Nerr =np.sqrt(N*60)/60
def f(U, a, b):
    return a * U + b

params, covariance_matrix = curve_fit(f, U, N)

errors = np.sqrt(np.diag(covariance_matrix))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print(a, b)
U_plot = np.linspace(330, 670)


plt.errorbar(U, N, Nerr, fmt='x', label='Werte mit Fehler')
#plt.plot(U, N, 'bx', label="werte")
plt.plot(U_plot, f(U_plot, *params), 'g-', label='linearer Fit', linewidth=2)
plt.xlabel('U/V')
plt.ylabel(r'$\frac{N}{\Delta t}/\frac{1}{s}$')
plt.legend(loc="best")
plt.savefig('Alina2.pdf')
