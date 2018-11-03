from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

A_M_fern, A_M_nah, dt_M = np.genfromtxt('Mes.txt', unpack = True)
rho_M = 8520
c_M = 385
Kappa_M = (rho_M * c_M * 0.04**2)/(2*dt_M* np.log(A_M_nah/A_M_fern))

Kappa_M_mean = ufloat(np.mean(Kappa_M), stats.sem(Kapa_M))

print(Kappa_M)
print('Kappa_M:', Kappa_M_mean)
