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

dU, dt = np.genfromtxt ("Messwerte/Mess1.txt",unpack=True, skip_header=3)
#U=np.log(dU)
dt=dt*10**-6

def f(dt,A,b):
    return A*np.exp(-2*np.pi*b*dt)

params, covariance = curve_fit(f, dt, dU)
errors = np.sqrt(np.diag(covariance))
print ("A=", params[0] ,"+-", errors[0])
print ("b=", params[1] ,"+-", errors[1])

plt.plot(dt, f(dt, *params), 'b-', label='Ausgleichskurve', linewidth=1)
plt.legend(loc="best")

plt.plot(dt, dU, "rx", label="Messwerte")
plt.xlabel(r"$t\,/\,\si{\micro\second}")
plt.ylabel(r"$ \Delta\mathrm{U} \, / \, \si{\volt}")
plt.xticks([0.00005, 0.00010, 0.00015, 0.00020],
           ['$50$', r'$100$', r'$150$', r'$200$'])
plt.legend(loc="best")
plt.xlim(min(dt-4*10**-6),max(dt+4*10**-6))
plt.yscale("log")
plt.ylim(0, max(dU+2))
plt.grid()


plt.tight_layout()
plt.savefig("Plotgedaempft.pdf")
