import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#I, D = np.genfromtxt('mess230e.txt' , unpack=True)
#D = D* 0.0252
I= 180*10**(-3)
µ= 4* np.pi *10**(-7)
N = 20
#R =0.282
#B = µ * 8/np.sqrt(125) *N*I/R
L = 0.1533
p=71*0.0175
B= 11.47*10**(-6)
#y = D/(L**2 + D**2)
A = B/np.cos(p)
print(B,A)
