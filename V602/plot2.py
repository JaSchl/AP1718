import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 18

t, Z = np.genfromtxt('ZirkoniumZ40.txt' , unpack=True)
x, y = np.genfromtxt('k.txt' , unpack=True)
#a, c = np.genfromtxt('beta.txt' , unpack=True)

plt.plot(t, Z,'r-', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.plot(x, y, 'b--', label=r"K-Kante")
#plt.plot(a, c, 'g--', label=r"$K_{L_2}$")


plt.ylabel(r"$R(35kV)/Imp/s$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$2 \cdot \theta /° $")
#plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best")
plt.savefig('zirkonium.pdf')
