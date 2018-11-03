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

R = 509.5
C = 2.098*10**-9
L = 10.11*10**-3


v, Uc, UcU = np.genfromtxt("Messwerte/Mess2.txt", unpack = True, skip_header=3)
U0 = 6.8
v = v*10**3
Uc = UcU / U0
x1 = np.linspace(15000, 40000, 100)
w1 = 2*np.pi*x1
Uv1=1/(np.sqrt((1-L*C*w1**2)**2+w1**2*R**2*C**2))


plt.plot(x1, Uv1, 'b-', label ="Theoriekurve")
plt.plot(v, UcU, 'rx', label="Messwerte", linewidth=1)
plt.xlabel(r"$\nu\,/\,\si{\hertz}$")
plt.ylabel(r"$\frac{U_\text{C}}{U}$")

plt.legend(loc='best')
#plt.xlim(min(w), max(w))
plt.grid()
plt.tight_layout()
plt.savefig("PlotUcUv.pdf")
