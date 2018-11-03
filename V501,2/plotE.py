import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

D, U = np.genfromtxt('mess230b.txt' , unpack=True)
D = D*0.0252
x=U
def f(U, m, n):
    return U*m + n
paramsI, covarianceI = curve_fit(f, x, D) #das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print(m, n)


L1plot = np.linspace(-25, 12) #Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.title('Ablenkung bei $400\, \mathrm{V}$') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(x, D,'r+', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$D/m$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$U_D/V$")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('plot230b.pdf')
