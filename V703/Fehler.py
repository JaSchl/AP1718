from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
import scipy.constants as const

#Fehler Totzeit
#n1 = ufloat (228.383, 1.95)
#n2 = ufloat (294.1, 2.21)
#n3 = ufloat (512, 2.92)
#
#T = (n1 + n2 -n3) / (2*n1*n2)
#
#print(T)
#
#
## Standartabweichung
#
##T = np.array[200, 201, 230]
##E = np.array[0.86, 1.28, 1.08]
##
##sem(T)
##sem(E)
#
#
#Teilchenzahl

U, N, I = np.genfromtxt('werte.txt', unpack=True)
N = N/60
I = I* 10**(-6)

Q = I / N
Q = Q/const.e
Q2 = (I / N**2) * (np.sqrt(N*60) /60)
Q2 = Q2 / const.e
print(Q2)


#Steigung

#a = ufloat(0.039, 0.004)
#b = ufloat(213.1, 2.2)
#U = 540
#f1 = ufloat(233, 3)
#f2 = ufloat(229.1, 2.7)
#f = U*a + b
#Q = ((f1/f2)-1)*100
#
#print(Q)
#print(f)


#Dleta Q / e_0 Fehler
