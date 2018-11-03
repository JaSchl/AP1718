import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

U, N = np.genfromtxt('1.txt' , unpack = True)
N = N/60
sN=np.sqrt(N*60)/60
plt.errorbar(U, N, yerr=sN, fmt='.b', label = 'Messwerte mit Fehlerbalken')

#x, y = np.genfromtxt('2.txt' , unpack=True)
#x = x/60
#y = y/60

def f(U, a, b):
    return U*a + b
paramsI, covarianceI = curve_fit(f, U, N)
errorsI = np.sqrt(np.diag(covarianceI))
a = ufloat(paramsI[0], errorsI[0])
b = ufloat(paramsI[1], errorsI[1])
print(a, b)

L1plot = np.linspace(330 , 670)
plt.xlabel(r'U / V') #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.ylabel(r"N")
plt.plot(L1plot, f(L1plot, *paramsI) , 'r-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best")

plt.savefig('1.pdf')


#a=0.6+/-0.5, b= (1.133+/-0.025)e+04
