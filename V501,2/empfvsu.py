import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

m, U = np.genfromtxt('empfindlichkeit.txt' , unpack=True)
U = 1/U * 10**3
m = m*10**3
def f(U, a, n):
    return U*a + n
paramsI, covarianceI = curve_fit(f, U, m) #das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
a = ufloat(paramsI[0], errorsI[0])
print(a, n)


L1plot = np.linspace(2.45, 4.5) #Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.title('Empfindlichkeit gegen $1/U_B$') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(U, m,'r+', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$\left(\frac{D}{U_d} \, / \, \, \frac{N}{C}\right)\, \cdot 10^{-3}$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$\left(U_B^{-1} / V^{-1}\right) \, \cdot 10^{-3}$")
plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('empfvsu.pdf')
