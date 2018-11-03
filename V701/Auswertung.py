import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
from scipy.stats import norm
from scipy.misc import factorial
import scipy

p1, C1, N1_g, N1 = np.genfromtxt('werte15.txt', unpack=True)
#hier werden die Werte eingelesen: Druck, Counts, Channel, impulses detectet
p2, C2, N2_g, N2 = np.genfromtxt('werte2.txt', unpack=True) #zweite Messung mit anderem Abstand
N3 = np.genfromtxt('e.txt', unpack=True) #Statistikmessung

#Plot1a x:Reichweite y:Zählrate____________________________________________________
#plt.figure(1)
x1_0 = 1.5 #Abstand der Quelle und des Detektors (vielleicht ändern), in cm
p_0= 1013

x1 = x1_0 * p1/p_0
r1=N1_g /120

#L1plot = np.linspace(0.75, 1.5) #musst du nur noch anpassen
#def f1(x1, s1, b1):
#    return x1*s1+b1
#paramsI, covarianceI = curve_fit(f1, x1[12:], r1[12:]) #hier wird durch die eckige Klammer nur ein Teil der Werte genommen (von Wert 15 bis Ende)
##musst du dann bei dir gucken, welche Werte du davon alle nimmst für die lineare Regression
#errorsI = np.sqrt(np.diag(covarianceI))
#b1 = ufloat(paramsI[1], errorsI[1])
#s1 = ufloat(paramsI[0], errorsI[0])
#print('1. MESSUNG (x:Reichweite, y: Zählrate)')
#print('Steigung der linReg:', s1)
#print('y-Achsenabschnitt der linReg:', b1)
#
#plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
#plt.plot(x1, r1, 'bx', label = 'Messwerte')
#plt.xlabel(r"$x / \mathrm{cm}$")
#plt.ylabel(r"$R / \mathrm{\frac{1}{s}}$")
#plt.axhline(y=394.725, color='c', linestyle='--', label=r"$y=\frac{R(x=0)}{2}$")
#plt.axvline(x=1.11, color='c', linestyle='-.' ,label=r"$R_m=1.10 \, \mathrm{cm}$")
##Werte der horizontalen und vertikalen Linie müssen angepasst werden
#plt.tight_layout()
#plt.legend(loc="best")
#plt.savefig('mreich1.pdf')
#
EX1=(11.1/3.1)**(2/3)#mittlere Reichweite muss angepasst werden (also statt 15.3): x-Wert der vertikalen Linie in mm (nicht cm!))
print('Energie der mittleren Reichweite:', EX1, 'MeV')
##
#Plot1b x:Druck y:Energie_________________________________________________________
plt.figure(2)
E_0=4
E1 = C1/951*E_0 #hier musst du deinen ersten Counts-wert eintagen für p=0 statt der 951
plt.plot(p1, E1, 'b.', label='Messwerte')
L1plot = np.linspace(0, 1000)
def f1(p1, m1, n1):
    return m1*p1+n1
paramsI, covarianceI = curve_fit(f1, p1, E1)
errorsI = np.sqrt(np.diag(covarianceI))
n1 = ufloat(paramsI[1], errorsI[1])
m1 = ufloat(paramsI[0], errorsI[0])
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.xlabel(r"$p / \mathrm{mbar}$")
plt.ylabel(r"$E / \mathrm{MeV}$")
plt.tight_layout()
plt.legend(loc="best")
#plt.savefig('Messung1b.pdf')
#print()
#print('1. MESSUNG (x:Druck, y:Energie)')
#print('Steigung der linReg: ', m1)
#print('y-Achsenabschnitt der linReg: ', n1)

#Plot1c (Energieverlust) x:mittlereReichweite y: Energie__________________________________________________
plt.figure(3)
L1plot = np.linspace(0, 1.2)
def f1(x1, m3, n3):
    return x1*m3+n3
paramsI, covarianceI = curve_fit(f1, x1, E1)
errorsI = np.sqrt(np.diag(covarianceI))
n3 = ufloat(paramsI[1], errorsI[1])
m3 = ufloat(paramsI[0], errorsI[0])
plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
plt.plot(x1, E1, 'bx', label='Messwerte')
plt.xlabel(r"$x / \mathrm{cm}$")
plt.ylabel(r"$E / \mathrm{MeV}$")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Messung1c.pdf')
print()
print('1.MESSUNG (x:effektiveLänge, y:Energie)')
print('Energieverlust(-dE/dx)', -m3)
print('y-Achsenabschnitt: ', n3)
#
##Plot2a x:Reichweite y:Zählrate____________________________________________________
#plt.figure(4)
#x2_0 = 2 #das muss wieder ggf angepasst werden, (Abstand Quelle-Detektor)
#p_0= 1013
#
#x2 = x2_0 * p2/p_0
#r2=N2_g/120 #erneut das Zeitintervall 120s, muss ggf noch angepasst werden
#
#L1plot = np.linspace(0.7, 2)
#def f1(x2, s2, b2):
#    return x2*s2+b2
#paramsI, covarianceI = curve_fit(f1, x2[9:], r2[9:]) #hier wird wieder nur ein Teil der Werte genommen
#errorsI = np.sqrt(np.diag(covarianceI))
#b2 = ufloat(paramsI[1], errorsI[1])
#s2 = ufloat(paramsI[0], errorsI[0])
#print()
#print('2. MESSUNG (x:Reichweite, y:Zählrate)')
#print('Steigung der linReg:', s2)
#print('y-Achsenabschnitt der linReg:', b2)
#plt.plot(L1plot, f1(L1plot, *paramsI) , 'g-', label="Lineare Regression")
#
#plt.plot(x2, r2, 'bx', label = 'Messwerte')
#plt.xlabel(r"$x / \mathrm{cm}$")
#plt.ylabel(r"$R / \mathrm{\frac{1}{s}}$")
#plt.axhline(y=307.025, color='c', linestyle='--', label=r"$y=\frac{R(x=0)}{2}$")
#plt.axvline(x=1.21, color='c', linestyle='-.' ,label=r"$R_m=1.21 \, \mathrm{cm}$")
##Werte der horizontalen und vertikalen Linie müssen angepasst werden
#plt.tight_layout()
#plt.legend(loc="best")
#plt.savefig('mreich2.pdf')
#EX2=(12.1/3.1)**(2/3) #Auch hier muss mittlere Reichweite angegeben werden(in mm)
#print('Energie der mittleren Reichweite:', EX2, 'MeV')
##
##Histogramm mit Verteilungen
#plt.figure(5)
#print()
#print('STATISTIK:')
#t = np.linspace(6800, 8000) #hier musst du nur deinen Linspace und ggf die Anzahl der bins verändern
#nu = sum(N3)/103
#print('Mittelwert: ', nu)
#sigma = (sum((N3-nu)**2)/(102))**(1/2)
#print('Abweichung: ', sigma)
#plt.hist(N3,  bins=18, normed=True, label='Messwerte')
#p_p= np.random.poisson(nu, 10000)
#plt.hist(p_p, bins=18, color='g', alpha=0.5, normed=True, label='Poissonverteilung')
#p_n= np.random.normal(nu, sigma, 10000)
#plt.hist(p_n, bins=18, color='r', alpha=0.5, normed=True, label='Normalverteilung')
#plt.legend(loc="best")
#plt.xlabel(r"$Counts$")
#plt.ylabel(r"$p(Counts)$")
#plt.savefig('Statistik.pdf')



#tabellen erstellen
#z = np.genfromtxt('zahlen.txt' , unpack=True)
#np.savetxt('Tabelle1.txt', np.column_stack([p1, N1, C1, N1_g, E1]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.2f')
#np.savetxt('Tabelle2.txt', np.column_stack([p2, N2, C2, N2_g]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.0f')
#np.savetxt('Tabelle3.txt', np.column_stack([z[0:25], N3[0:25], z[25:50], N3[25:50], z[0:25], N3[50:75], z[25:50], N3[75:100] ]), delimiter=' & ', newline= r' \\'+'\n', fmt='%.0f')
