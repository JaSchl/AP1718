import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x,y,z = np.genfromtxt('Messwerte/b.txt', unpack=True)
y = y/21.6
def f(x, b):
    return 1/np.sqrt(1+(x/(2*np.pi))**2 * b**2)

params, cov = curve_fit(f, x, y)
x_plt = np.logspace(1, 5)

plt.plot(x, y, 'rx', label='Messwerte')
plt.plot(x_plt, f(x_plt, *params), 'k-', label='Fit')

plt.xlabel(r'$\nu \:/\: \si{\hertz}$')
plt.ylabel(r'$U_\text{C} \:/\: U_0$')
plt.xscale('log')
plt.xlim(9,10**5)
plt.ylim(-0.05, 1.05)

plt.legend(loc='best')

print('Parameter: ', params, '\nFehler: ', np.sqrt(np.diag(cov)))

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/b1.pdf')
