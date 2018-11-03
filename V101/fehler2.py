from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

T = ufloat (1.568, 0.017)
D = ufloat (0.032, 0.007)
I = ufloat (0.0035, 0.0012)

Z = ((T**2 * D) / (np.pi**2 * 4)) -I

print(Z)
