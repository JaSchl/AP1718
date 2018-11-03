import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16


U, N = np.genfromtxt('1.txt', unpack=True)
N = N/60
Nerr =np.sqrt(N*60)/60 #?? sehr kleine Balken wenn 60 außerhalb der klammer



U_plot = np.linspace(170, 200)


plt.errorbar(U, N, Nerr, fmt='x', label='Werte mit Fehler')
#plt.plot(U, N, 'bx', label="werte")
plt.plot(np.ones(200) * 350, np.linspace(170, 210, 200), 'b--', label = r'Beginn des Pleateau-Bereiches')
plt.plot(np.ones(200) * 610, np.linspace(170, 210, 200), 'g--', label = r'Ende des Plateau-Bereiches')


plt.xlabel('U/V')
plt.ylabel(r'$\frac{N}{\Delta t}/\frac{1}{s}$')
plt.legend(loc="best")
plt.savefig('Alina1.pdf')
