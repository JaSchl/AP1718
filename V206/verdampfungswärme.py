import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

x, y = np.genfromtxt('druck.txt' , unpack=True)
T = 1/x
p = np.log(y)

def f(T, m, n,):
    return T * m + n
paramsI, covarianceI = curve_fit(f, T, p) #das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])

print(m, n)

L1plot = np.linspace(0.003, 0.0034)
plt.title('Dampfdruckkurve') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(T, p,'b+', label="$Messwerte$") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
plt.rcParams['font.size'] = 15
#Achsen beschriften!!!!!!
plt.ylabel('ln(p)') #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel('1/T')
plt.plot(L1plot, f(L1plot, *paramsI) , 'c-', label='$Regression$') #b- macht eine blaue durchgezogene Linie
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('verd.pdf') #erstellt und speichert automatisch den Plot als pdf datei
