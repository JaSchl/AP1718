import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1

U, I = np.genfromtxt('messdop.txt', unpack=True)
U = U - 20.5
I = I
l = 633*10**-6
L = 990.5

def T(g, b, h, l, x):
    return np.max(I) * np.cos(np.pi * g *np.sin(np.arctan((x-U[np.argmax(I)])/l))/h)**2*(h/(np.pi*b*np.sin(np.arctan((x-U[np.argmax(I)])/l))))**2 * np.sin(np.pi * b * np.sin(np.arctan((x-U[np.argmax(I)])/l))/h)**2

x_plot = np.linspace(-13, 13, 100000)

plt.plot(U, I, 'rx', label='Messwerte Doppelspalt')
plt.plot(x_plot, T(0.5, 0.15, 633*10**-6, 990.5, x_plot), 'b-', label='Theorie')

U2, I2 = np.genfromtxt('mess15.txt', unpack=True)
I2 = I2/ 413.3
U2 = U2- 20.5
def F(y, I0, c, y0):
    return I0**2 * c**2 * (l/(np.pi*c*np.sin((y-y0)/L)))**2 * (np.sin(np.pi * c * np.sin((y-y0)/L)/l))**2

params1, covariance1 = curve_fit(F, U2, I2, p0=[np.max(I2), 0.075, 0.1])

errors1 = np.sqrt(np.diag(covariance1))
print('         Parameter für die erste Linie: ')
print('             A =', params1[0], '±', errors1[0])
print('             b =', params1[1], '±', errors1[1])
print('             x0 =', params1[2], '±', errors1[2])
b = ufloat(params1[1], errors1[1])

y_plot = np.linspace(-21, 25, 100000)
plt.plot(y_plot, F(y_plot, params1[0], params1[1], params1[2]), 'g-', label='Einzelspalt')
#plt.plot(U2, I2, 'gx', label='Messwerte Einzelspalt')
#plt.plot(y_plot, F(0.5, 0.15, 633*10**-6, 990.5, y_plot), 'g-', label='Einzelspalt')
plt.legend(loc='best')
plt.ylabel(r'$I / \mathrm{µA}$')
plt.xlabel(r'$x / \mathrm{mm}$')
# plt.xlim(9, 1e2)
# plt.ylim(1e1, 1e4)
plt.grid()
plt.tight_layout()
plt.savefig('doppel2.pdf')
