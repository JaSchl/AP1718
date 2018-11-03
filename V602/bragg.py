import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

t, Z = np.genfromtxt('Bragg.txt' , unpack=True)

#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
#def f(t, m, n):
#    return t*m + n
#paramsI, covarianceI = curve_fit(f, Z, t) #das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
#errorsI = np.sqrt(np.diag(covarianceI))
#n = ufloat(paramsI[1], errorsI[1])
#m = ufloat(paramsI[0], errorsI[0])
#print(m, n)

L1plot = np.linspace(26, 30) #Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
#plt.title('Bragg') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(t, Z,'b+', label="Messwerte") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
#Achsen beschriften!!!!!!
plt.ylabel(r"$R(35kV)/Imp/s$") #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel(r"$2\cdot \theta$")
#plt.plot(L1plot, f(L1plot, *paramsI) , 'b-', label='Regression') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('bragg.pdf')
