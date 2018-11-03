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

v, Uc, U = np.genfromtxt("Messwerte/Mess2.txt", unpack = True, skip_header=3)

L=10.11*10**-3
C=2.098*10**-9
R=509.5
U0=6.8
x=np.linspace(29,40,100)
w1=2*np.pi*x*10**3
Uv=1/(np.sqrt((1-L*C*w1**2)**2+w1**2*R**2*C**2))

plt.plot(x,Uv,'b-', label='Theoriekurve')
plt.plot(v, U, 'rx', label="Messwerte", linewidth=1)
plt.plot((30.8, 30.8), (1.2, 4.4), 'g--')
plt.plot((38.8, 38.8), (1.2, 4.4), 'g--', label='Breite der Resonanzkurve')
plt.xlabel(r"$\nu\,/\,\si{\kilo\hertz}$")
plt.ylabel(r"$\frac{U_\text{C}}{U}$")
plt.xlim(29,40)
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig("PlotRes.pdf")
