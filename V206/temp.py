import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#erstelle eine .txt Datei, aus der die Werte fuer die Funktion genommen werden koennen. Das, was in der ersten Spalte steht, sind automaisch die x-Werte,
#die zweite die y-Werte.

x, y = np.genfromtxt('temp1.txt' , unpack=True)
a, b = np.genfromtxt('temp2.txt' , unpack=True)
#linregress vorbereitung(Fkt definieren m=Steigung, n=y-Schnittpkt)
def f(x, m, n, o):
    return (x**2) * m + n * x + o
paramsI, covarianceI = curve_fit(f, x, y) #das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsI = np.sqrt(np.diag(covarianceI))
o = ufloat(paramsI[2], errorsI[2])
n = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])

print(m, n, o) #Dieser Befehl gibt euch in der Kommandozeile als ersten Wert fuer m mit Fehler und den zweiten Wert
#fuer n wieder mit Fehler.
def g(a, c, d, e):
    return (a**2) * c + a * d + e
paramsII, covarianceII = curve_fit(g, a, b ) #das muss hier einfach alles hin...kann nicht genau sagen, was es macht.
errorsII = np.sqrt(np.diag(covarianceII))
e = ufloat(paramsII[2], errorsII[2])
d = ufloat(paramsII[1], errorsII[1])
c = ufloat(paramsII[0], errorsII[0])
print(c, d, e)

#with plt.xkcd(): (macht, dass die ganze Sache in comic sans ms optik ausgegeben wird. Sieht sehr fein aus, ist aber vielleicht nicht sooo wichtig)
#Plot der Messwerte:

L1plot = np.linspace(0, 1150)
L2plot = np.linspace(0, 1150)#Grenzen fuer linregr. guckt nach den Grenzwerten fuer die x-Werte.
plt.title('Temperaturverlauf') #Ueberschrift, die ueber dem PLot stehen wird
plt.plot(x, y,'b+', label="$Messwerte T_1$") #r+, macht, dass eure Werte als rote Plusse erscheinen. mit b* kommen blaue sterne...mehr Farben kann man online finden;)
plt.plot(a, b,'k+', label="$Messwerte T_2$")
#Achsen beschriften!!!!!!
plt.ylabel('Temperatur/K') #hier wurde Tex Code verwendet, um Brueche ordentlich darzustellen. das T_P macht, dass das P als Indesx von T erscheint. Hinter den Slash kommt die Einheit fuer die jeweilige Groesse
plt.xlabel('Zeit/s')
plt.plot(L1plot, f(L1plot, *paramsI) , 'c-', label='$Ausgleichsfunktion T_1$') #b- macht eine blaue durchgezogene Linie
plt.plot(L2plot, g(L2plot, *paramsII) , 'r-', label='$Ausgleichsfunktion T_2$')
plt.tight_layout #macht irgendwas schoener. einfach dran machen...
plt.legend(loc="best") #macht die Legende an den Ort innerhalb des Plots, wo am meisten Platz dafuer ist.

plt.savefig('temp.pdf') #erstellt und speichert automatisch den Plot als pdf datei
