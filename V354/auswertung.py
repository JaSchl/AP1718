import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import stats
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 18

#Teil a)
#Einlesen der Daten
finkHz, dtinmus, UcindV, UerinV  = np.genfromtxt('messwerte.txt', unpack=True)
UtiindV, tiinmus = np.genfromtxt('messwerte_obere_einh.txt', unpack=True)
dt = dtinmus * 10**(-6)
Uc = UcindV/10
UerinV = UerinV/100
Uti = UtiindV/10
tiins = tiinmus * 10**(-6)
#Fitten der e-Funktion
def f(t, A, mu):
    return A*np.exp(mu*t)
params, covariance = curve_fit(f, tiins, Uti)
errors = np.sqrt(np.diag(covariance))
A = ufloat(params[0], errors[0])
mu = ufloat(params[1], errors[1])

#Berechnen von R unt T und Ausgabe
L=ufloat(10.11, 0.03)*10**(-3)
mu=mu/(-2*np.pi)
R = (mu * 4 * np.pi * L)
T = 2*L/R
print("Ao: ",A)
print("mu: ",mu)
print("Reff: ", R)
print("Teff: ",T)


#Teil b)
#Berechnen von Rap
C = ufloat(2.098, 0.006) * 10**(-9)
Rap = unp.sqrt((4*L)/(C))
print("Rap: ",Rap)

#Teil c)
#Halblogarithmische Darstellung der Kondensatorspannung U=Uc/Uer
U = Uc/UerinV
print(Uc)
print(UerinV)
print(U)
R2 = ufloat(509.5, 0.5)
w0 = unp.sqrt(1/(L*C))
qerr = 1/(w0*R2*C)
print(qerr)
print("Breite der Resonanz: ", R2/(L*2*np.pi))
np.savetxt('Quotienten.txt', np.column_stack([finkHz, unp.nominal_values(U)]),fmt="%.3f")

plt.figure(2)
plt.xlabel(r"$\nu / 10^3 \, \mathrm{Hz}$")
plt.ylabel(r"$\frac{U_\mathrm{C}}{U_\mathrm{err}}$")
plt.xscale("log")
plt.grid()
plt.plot(finkHz*1000, U, 'b+', label='Messwerte')
plt.legend(loc="best")
plt.tight_layout
plt.savefig('Halblog.pdf')

plt.figure(3)
plt.grid()
plt.xlim(19,41)
plt.ylim(1, 4.1)
plt.xlabel(r"$\nu / \mathrm{Hz}$")
plt.ylabel(r"$\frac{U_\mathrm{C}}{U_\mathrm{err}}$")
plt.plot(finkHz, U, 'b+', label='Messwerte')

plt.xticks([20, 25, 29.5, 34, 35, 38.5, 40],
           ["20", "25", "29.5", "34", "35", "38.5", "40"])
plt.axvline(x=29.5, ymin=0, ymax=0.57, color='g', ls="--", label=r"$\nu_+$ bzw. $\nu_-$", linewidth=2)
plt.axhline(y=4, xmin=0, xmax=0.681, color='r', ls="--", linewidth=2)
plt.axvline(x=38.5, ymin=0, ymax=0.57, color='g', ls="--", linewidth=2)
plt.axvline(x=34, ymin=0, ymax=0.9677, color='r', ls="--", label="Resonanzüberhöhung", linewidth=2)
plt.axhline(y=2.75, xmin=0.48, xmax=0.8864, color='y', label="Resonanzbreite", ls="--", linewidth=2)
plt.legend(loc="best")
plt.tight_layout
plt.savefig('lin.pdf')

#Teil d)
T=1/(finkHz*10**3)
phi = 360*dt/T
print(phi)

wres = 1/(2*np.pi) * unp.sqrt( ( 1 / (L*C) ) - ( (R2**2) / (2*L**2) ) )
w1 = 1/(2*np.pi) * ( R2/(2*L) + unp.sqrt( ( 1 / (L*C) ) + ( (R2**2) / (4*L**2) ) ) )
w2 = 1/(2*np.pi) * ( -R2/(2*L) + unp.sqrt( ( 1 / (L*C) ) + ( (R2**2) / (4*L**2) ) ) )
print("Wres: ", wres)
print("W1: ", w1)
print("W2: ", w2)
np.savetxt('Phasen.txt', np.column_stack([finkHz, dtinmus, T*10**(6), phi]),fmt="%.3f")


plt.figure(4)
plt.xlabel(r"$\nu / \mathrm{Hz}$")
plt.ylabel(r"$\varphi / \mathrm{rad}$")
plt.grid(True, which="both")
plt.ylim(0,200)
plt.xlim(20,41)
plt.xscale("log")
plt.yticks([0, 45, 90, 135, 180],
           [r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.plot(finkHz*1000, phi, 'b+', label='Messwerte')
plt.legend(loc="best")
plt.tight_layout
plt.savefig('Phasehalblog.pdf')

plt.figure(5)
plt.xlabel(r"$\nu / 10^3 \, \mathrm{Hz}$")
plt.ylabel(r"$\varphi / \mathrm{rad}$")
plt.grid()
plt.ylim(0,200)
plt.xlim(20,41)
plt.yticks([0, 45, 90, 135, 180],
           [r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.xticks([20, 25, 30, 31, 35, 39, 40],
            ["20", "25", "30", "31", "35", "39", "40"])
plt.plot(finkHz, phi, 'b+', label='Messwerte')
plt.axhline(y=90, xmin=0, xmax=0.714, color='r', ls="--", label='Resonanz', linewidth=2)
plt.axhline(y=45, xmin=0, xmax=0.524, color='g', ls="--", label=r'$\nu_1$ bzw. $\nu_2$', linewidth=2)
plt.axhline(y=135, xmin=0, xmax=0.905, color='g', ls="--", linewidth=2)
plt.axvline(x=31, ymin=0, ymax=0.225, color='g', ls="--", linewidth=2)
plt.axvline(x=39, ymin=0, ymax=0.675, color='g', ls="--", linewidth=2)
plt.axvline(x=35, ymin=0, ymax=0.45, color='r', ls="--", linewidth=2)
plt.legend(loc="best")
plt.tight_layout
plt.savefig('Phaselin.pdf')

np.savetxt('Tabelle.txt', np.column_stack([finkHz, UcindV, UerinV, unp.nominal_values(U), dtinmus, T*10**(6), phi]),fmt="%.3f")
