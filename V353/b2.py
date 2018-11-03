import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x,y,a = np.genfromtxt('Messwerte/b.txt', unpack=True)
b = 1000/x
z = a/b * 2*np.pi

def f(x, a):
    return np.arctan(-(x/(2*np.pi))*a)

params, cov = curve_fit(f, x, z)
x_plt = np.logspace(1, 5)

plt.plot(x, z, 'rx', label='Messwerte')
plt.plot(x_plt, f(x_plt, *params), 'k-', label='Fit')

plt.xlabel(r'$\nu \:/\: \si{\hertz}$')
plt.ylabel(r'$\phi \:/\: \si{rad}$')
plt.xscale('log')

plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/b2.pdf')
#print('Parameter: ', params, '\nFehler: ', np.sqrt(np.diag(cov)))
