from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

a = ufloat (0.247, 0.005)
b = ufloat (-0.73, 0.07)
c = ufloat (1, 7)

x = (1/2 * unp.log(( 1 + (-c/693))/(1 +(-c/693)))/a) - b

print(x)
