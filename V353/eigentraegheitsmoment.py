import numpy as np
from astropy.io import ascii
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d, T_messung = np.genfromtxt('rohdaten/data2.txt', unpack=True)
abstand = unp.uarray(d, 0.05)  # in cm
abstand *= 1e-2  # Umrechnung von cm in m
T = unp.uarray(T_messung, 0.05)  # in s
T = T / 5  # Es wurden fünf Perioden gemessen


# Standardabweichung des Mittelwerts
def meanDerivation(a):  # a ist ein Array
    N = len(a)  # Anzahl an Messwerten
    temp = 0.
    mittelwert = np.mean(a)  # Mittelwert der Messwerte
    for value in a:
        temp += (value-mittelwert)**2
    temp *= 1/(N*(N-1))
    return unp.sqrt(temp)

# "masselose" Stange
m_stange = ufloat(96.29, 0.01)  # in g
m_stange *= 1e-3  # Umrechnung von g in kg
Durchmesser_stange = [0.00485, 0.00480, 0.00480, 0.00495, 0.00480]  # in m
r_stange = ufloat(np.mean(Durchmesser_stange), meanDerivation(Durchmesser_stange))  # Ist noch der Durchmesser
r_stange *= 0.5  # Nun ist es der Radius
l_stange = ufloat(0.29985, 0.00001)  # laenge der Stange in m
l_stange *= 2  # Das vorherige war pro Seite
I_stange = m_stange*(l_stange**2)/12
print("Mittelwert und Standardabweichung des Radius' der Stange")
print(np.mean(Durchmesser_stange), meanDerivation(Durchmesser_stange))
print("Trägheitsmoment der \"masselosen\" Stange")
print(I_stange)


# Trägheitsmoment der Massen
def I_Zylinder(m, R, h):
    temp = (R**2)/4 + (h**2)/12
    temp *= m
    return temp


# Satz von Steiner, Verschiebung um a
def Steiner(I, m, a):
    return I + m*(a**2)


# Gewichte
m_c = ufloat(223.42, 0.01)  # Gewicht in g
d_c = ufloat(3.490, 0.001)  # Durchmesser Gewicht C in cm
h_c = ufloat(3.015, 0.001)  # Höhe Gewicht C in cm
m_b = ufloat(222.50, 0.01)  # Gewicht in g
d_b = ufloat(3.485, 0.001)  # Durchmesser Gewicht B in cm
h_b = ufloat(3.000, 0.001)  # Höhe Gewicht B in cm
d_c *= 1e-2  # Umrechnung von cm in m
h_c *= 1e-2  # Umrechnung von cm in m
d_b *= 1e-2  # Umrechnung von cm in m
h_b *= 1e-2  # Umrechnung von cm in m
m_c *= 1e-3  # Umrechnung von g in kg
m_b *= 1e-3  # Umrechnung von g in kg
I_c = I_Zylinder(m_c, d_c/2, h_c)
I_b = I_Zylinder(m_b, d_b/2, h_b)
# I_c = Steiner(I_c, m_c, abstand+h_c/2)
# I_b = Steiner(I_b, m_b, abstand+h_b/2)
print("Trägheitsmoment von Gewicht C ohne Steiner:")
print(I_c)
print("Trägheitsmoment von Gewicht B ohne Steiner:")
print(I_b)


# Fitfunktion
def f(x, m, b):
    return m * x + b


# Lineare Regression
alpha = abstand + h_c/2  # Da der Abstand nicht von der Zylindermitte gemessen wurde,
# sondern vom Rand
temp1 = alpha**2  # a² in m²
x = noms(temp1)
x_err = stds(temp1)
temp2 = T**2  # T² in s²
y = noms(temp2)
y_err = stds(temp2)
print('T² in s²:    ', y)
print('a² in m²:    ', x)
x_plot = np.linspace(0, 0.1)
params, covariance = curve_fit(f, x, y)
# covariance is the covariance matrix
errors = np.sqrt(np.diag(covariance))
print('Parameter für Data 2 gefittet: ')
print('     m =', params[0], '±', errors[0])
print('     b =', params[1], '±', errors[1])

# Plot
plt.errorbar(x*1e2, y, xerr=x_err*1e2, yerr=y_err, fmt='rx', label='Messwerte')
# plt.plot(x*1e2, y, 'rx', label='Messwerte')
plt.plot(x_plot*1e2, f(x_plot, *params), 'b-', label='Regression')
plt.legend(loc='best')
plt.xlabel(r'$\alpha^2 \; / \; 10^2\mathrm{m^2}$')
plt.ylabel(r'$T^2 \; / \; \mathrm{s^2}$')
plt.xlim(0.5, 8)
plt.ylim(10, 70)
plt.grid()
plt.tight_layout()
# plt.show()
plt.savefig('build/plot_eigen.pdf')
plt.clf()

# Eigenträgheitsmoment I_D ausrechnen
m = ufloat(params[0], errors[0])  # in m²/s²
b = ufloat(params[1], errors[1])  # in s²
# I = I_D + I_c + I_b + I_stange
D = (4*(np.pi**2) * (m_b + m_c)) / m
# D_1 = ufloat(0.000381, 0.000007)  # Aus Aufgabenteil 1
I_D = b*D/(4*(np.pi**2)) - (I_stange + I_b + I_c)
print("D aus dem Fit berechnet:")
print(D)
print("Eigenträgheitsmoment des Aufbaus aus dem Fit berechnet:")
print("(Dazu wurde das D aus dem Fit verwendet)")
print(I_D)

# Ergebnisse speichern
x *= 1e2  # Umrechnung m in cm
x_err *= 1e2
x = np.round(x, 3)
x_err = np.round(x_err, 3)
y = np.round(y, 2)
y_err = np.round(y_err, 2)
abstand *= 1e2
ascii.write(
    [noms(abstand), T_messung, y, y_err, x, x_err],
    'build/table_eigen.tex', format='latex')