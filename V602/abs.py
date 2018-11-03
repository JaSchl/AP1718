import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const

x, c = np.genfromtxt('z.txt', unpack=True)
c = c*10**(3)
y = np.sqrt(c*const.e)
def f(x, a, b):
    return a * x + b

paramsI, covariance_matrix = curve_fit(f, x, y)

errorsI = np.sqrt(np.diag(covariance_matrix))

a = ufloat(paramsI[0], errorsI[0])
b = ufloat(paramsI[1], errorsI[1])

print(a, b)
#matplotlib inline
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
#plt.rcParams['lines.linewidth'] = 3

L1plot = np.linspace(34.9, 40.1) #Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.title('Zylindrischer Stab, einseitige Einspannung') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(x, y,'go', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$\sqrt{E}/\sqrt{eV}$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"Z")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('Z.pdf') #erstellt und speichert automatisch den Plot als pdf datei
