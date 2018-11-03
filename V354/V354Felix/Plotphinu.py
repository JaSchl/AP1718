import matplotlib as mpl
from scipy.optimize import curve_fit
mpl.use('pgf')
import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 1
import numpy as np

mpl.rcParams.update({
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}'
})

v, t, phi, phi2 = np.genfromtxt("Messwerte/Mess3.txt", unpack = True, skip_header = 3)
R = 509.5
L = 10.11 * (10**-3)
C = 2.098 * (10**-9)
v = v*10**3
w = 2*np.pi*v


x1 = np.linspace(15000, 34500, 100)
x1 = 2*np.pi*x1
f = np.arctan((x1 * R * C) / (1 - (x1**2 * L * C)))
x2 = np.linspace(35000, 55000, 100)
x2 = 2*np.pi*x2
f2 = np.pi + np.arctan((x2 * R * C) / (1 - (x2**2 * L * C)))


plt.plot(x1, f, 'b-', label = 'Theoriekurve')
plt.plot(x2, f2, 'b-')
plt.plot(w, phi2, 'rx', label='Messwerte')
plt.xlabel(r'$\omega\,/\, \si{\hertz}')
plt.ylabel(r'$\varphi')
plt.yticks(np.arange(0, 7*np.pi/6, np.pi/6),
    ['$0$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$'])
#plt.xscale('log')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('PlotPhiNu.pdf')
