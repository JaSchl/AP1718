from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
import scipy.constants as const

t= ufloat(0.71122167, 0.00174533)
d = 201.4*10**(-12)

l = 2*d*unp.sin(t)
#l= l* 10**(-12)
E = const.h * const.c / l
E = (E / const.e)
print('lambda:')
print(l)
print('Energie:')
print(E)

#SIGMAAAAs
Q1 = 8980
Qa = 8146
Qb = 8999
R= 13.6
z=29

s1 = z - (Q1/R)**(1/2)
s2 = 2*(Qa/R)**(1/2)-z+2*s1
s3 = 3*(Qb/R)**(1/2)-2*z+3*s1

print('s1, s2,s3')
print(s1)
print(s2)
print(s3)
