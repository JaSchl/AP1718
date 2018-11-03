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

#R = 509.5
#L = 10.11 * (10**-3)
#C = 2.098 * (10**-9)
#
#f = np.arctan (-(v * R * C) / (1 - (v**2 * L * C)))
#
#plt.plot(v, f, 'b-', label = 'Theoriekurve')
plt.plot(v, phi2, 'rx', label='Messwerte')
plt.plot((30.779, 30.779), (0, 1.75), 'g--', label='untere/obere Grenzfrequenz')
plt.plot((38.799, 38.799), (1.75, 3), 'g--')
plt.plot((34.088, 34.088), (1.25, 2.5), 'b--', label = 'Resonanzfrequenz')
#plt.plot((29.0, 31.0), (0.79, 0.79), 'b--', label = 'pi viertel')
#plt.plot((37.8, 39.1), (2.36, 2.36), 'b--', label = '3 pi viertel')
plt.yticks([np.pi/5, np.pi/4, 2*np.pi/4, 3*np.pi/4, np.pi],
           ['$\frac{\pi}{5}$', r'$\frac{\pi}{4}$', r'$\frac{2\pi}{4}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
plt.xlabel(r'$\nu\,/\, \si{\kilo\hertz}')
plt.ylabel(r'$\varphi')
plt.xlim(27.000, 40.000)
plt.ylim(0.70, 2.8)
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('PlotPhiNuLin.pdf')
