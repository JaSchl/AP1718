from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

n = ufloat (4.3, 1.1)
D= ufloat (0.032, 0.007)


I= D / (4*((np.pi)**2)) * n - 1.14738*10**(-5)

print(I)
