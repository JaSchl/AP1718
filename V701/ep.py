import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 18


p, E = np.genfromtxt('werteep2.txt', unpack=True)

def f(p, a, b):
    return a * p + b

params, covariance_matrix = curve_fit(f, p[:14], E[:14])

errors = np.sqrt(np.diag(covariance_matrix))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print(a, b)
#matplotlib inline


x_plot = np.linspace(-50, 650)

plt.plot(p, E, 'k+', label="Werte")
plt.plot(x_plot, f(x_plot, *params), 'g-', label='linearer Fit', linewidth=3)
plt.legend(loc="best")
plt.xlabel(r"$p / \mathrm{mbar}$")
plt.ylabel(r"$E / \mathrm{MeV}$")
plt.savefig('ep2.pdf')
