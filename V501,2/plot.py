import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats


I, D = np.genfromtxt('mess230e.txt' , unpack=True)
D = D* 0.0252
#e = 1.6*10**(-19)
#m = 9.1 *10**(-31)
#I= I
µ= 4* np.pi *10**(-7)
N = 20
R =0.282
#U = 400
B = µ * 8/np.sqrt(125) *N*I/R
L = 0.1533
y = D/(L**2 + D**2) #1/np.sqrt(8*U) * np.sqrt(e/m) * B
x = B *10**5

def f(x, m, n):
    return x*m + n
paramsI, covarianceI = curve_fit(f, x, y)
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print(m, n)


L1plot = np.linspace(0, 15.5) #Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.title(r'$D/(L^2+D^2)$ gegen B') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(x, y,'r+', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$(D/(L^2+D^2))/m^{-1}$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$B/ T\cdot 10^{-5} $")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('plot230e.pdf')
