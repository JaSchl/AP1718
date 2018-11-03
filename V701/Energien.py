import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
from scipy.stats import norm
from scipy.misc import factorial
import scipy

#x = np.array([635, 631, 611, 596, 577, 567, 552, 528, 519, 510, 495, 479,
#456, 446, 440, 440, 440, 440, 439, 438])
##x = np.array([678, 661,
##590,
##574,
##556,
##531,
##523,
##559,
##534,
##523,
##502,
##447,
##443,
##441,
##438,
##438,
##439,
##435,
##463,
##434,
##435])
#E1 = 4/635
#
#E = x*E1
#
#print(E)

#effektive effektive
x_0 = 2
p_0 =1013
p1 = np.array([0, 50,
100,
150,
200,
250,
300,
350,
400,
450,
500,
550,
600,
650,
700,
750,
800,
850,
900,
950,
1000])

x = x_0 * p1/p_0


print('effektive Länge:')
print(x)
