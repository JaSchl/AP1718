import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x, y = np.genfromtxt('Messwerte/a.txt', unpack=True)
y = y/17.6
y = np.log(y)
x_plt = np.linspace(0, 0.1)

def f(x, a):
    return a*x
params, cov = curve_fit(f, x, y)

plt.plot(x, y, 'rx', label='Messwerte')
plt.plot(x, f(x, *params), 'k-', label='linearer Fit')

plt.xlabel(r'$t \:/\: \si{ms}$')
plt.ylabel(r'$\log(U_\text{C} \:/\: U_0)$')
plt.xlim(0, 1.1)
plt.legend(loc='best')

#print('Parameter: ', params, '\nFehler: ', np.sqrt(np.diag(cov)))

# in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/a.pdf')
