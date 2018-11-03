import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
from scipy.constants import constants



alpha = 1/137
Ryd = 13.6 * constants.e
d=201.4*10**(-12)

#KUPFER
Z_cu=29
print('KUPFER')
theta_alpha = 22.2
theta_beta = 20
E_alpha= constants.c*constants.h/(2*d*np.sin(theta_alpha/360*2*np.pi))
E_beta= constants.c*constants.h/(2*d*np.sin(theta_beta/360*2*np.pi))
E_alphaeV= constants.c*constants.h/(2*d*np.sin(theta_alpha/360*2*np.pi)) / constants.e
E_betaeV= constants.c*constants.h/(2*d*np.sin(theta_beta/360*2*np.pi)) / constants.e
print('E_alpha = ', E_alphaeV)
print('E_beta = ', E_betaeV)
theta_min = 5
E_max = constants.c*constants.h/(2*d*np.sin(theta_min/360*2*np.pi)) / constants.e
print('E_max = ', E_max)
lambda_min = 2*d*np.sin(theta_min/360*2*np.pi)
print('lambda_min = ', lambda_min)
sigma_K = Z_cu-(4*(E_beta-E_alpha) / Ryd)**(1/2)
print('sigma_K = ', sigma_K)



#LEICHTE ELEMENTE
print('LEICHTE ELEMENTE')
Z_brom = 35
Z_strontium = 38
Z_zirconium = 40
theta_brom = 26.1 / 2
theta_strontium = 21.7 /2
theta_zirconium = 19.5  /2
E_brom= constants.c*constants.h/(2*d*np.sin(theta_brom/360*2*np.pi))
E_strontium= constants.c*constants.h/(2*d*np.sin(theta_strontium/360*2*np.pi))
E_zirconium= constants.c*constants.h/(2*d*np.sin(theta_zirconium/360*2*np.pi))
E_bromeV= constants.c*constants.h/(2*d*np.sin(theta_brom/360*2*np.pi)) / constants.e
E_strontiumeV= constants.c*constants.h/(2*d*np.sin(theta_strontium/360*2*np.pi)) / constants.e
E_zirconiumeV= constants.c*constants.h/(2*d*np.sin(theta_zirconium/360*2*np.pi)) / constants.e
print('theta_brom = ', theta_brom)
print('theta_strontium = ', theta_strontium)
print('theta_zirconium = ', theta_zirconium)
print('E_brom in eV = ', E_bromeV)
print('E_strontium in eV = ', E_strontiumeV)
print('E_zirconium in eV = ', E_zirconiumeV)
sigma_K_brom = Z_brom-(E_brom / Ryd)**(1/2)
sigma_K_strontium = Z_strontium-(E_strontium / Ryd)**(1/2)
sigma_K_zirconium = Z_zirconium-(E_zirconium / Ryd)**(1/2)
print('sigma_K_brom = ', sigma_K_brom)
print('sigma_K_strontium = ', sigma_K_strontium)
print('sigma_K_zirconium = ', sigma_K_zirconium)


#QUECKSILBER
print('QUECKSILBER')
Z_qu=80
theta_L2=12.7
theta_L3=14.7

E_L2= constants.c*constants.h/(2*d*np.sin(theta_L2/360*2*np.pi))
E_L3= constants.c*constants.h/(2*d*np.sin(theta_L3/360*2*np.pi))
Delta_E = E_L2-E_L3
E_L2eV = E_L2 / constants.e
E_L3eV = E_L3 / constants.e
Delta_EeV = Delta_E/ constants.e
print('Energie L2 = ', E_L2eV)
print('Energie L3 = ', E_L3eV)
print('DeltaE = ', Delta_EeV)

sigma_L = Z_qu - (4/alpha*(Delta_E/Ryd)**0.5-5*Delta_E/Ryd)**0.5*(1+19/32*alpha**2*Delta_E/Ryd)**0.5
print('Sigma_L = ', sigma_L)

LINEARE REGRESSION
y, x = np.genfromtxt('lineareRegression.txt', unpack=True)
#x: ordnungszahl   y: energien in eV
y = (y*constants.e)**(1/2) #umrechnung in Joule und wurzel ziehen, da gengen wurzel(E) geplottet werden soll
L1plot = np.linspace(34,41)
def f1(x, m , b):
    return x*m+b
paramsI, covarianceI = curve_fit(f1, x, y)
errorsI = np.sqrt(np.diag(covarianceI))
b = ufloat(paramsI[1], errorsI[1])
m = ufloat(paramsI[0], errorsI[0])
print('Steigung der LinReg = ', m)
print('Y-Achsenabschnitt = ', b)
Ryd_berechnet = m**2 /constants.e
print('Ryd berechnet 0 ', Ryd_berechnet)
