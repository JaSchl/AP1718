from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
import matplotlib

T = ufloat (0.022, 0.005)
#B = ufloat (-0.05, 0.0024)


f= 13206 * T * 1/185

print(f)
