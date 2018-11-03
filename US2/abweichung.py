from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
import scipy.constants as const



theo = np.array([1.5, 6.3, 5.4, 4.6, 3.9,
3, 2.1, 1.3])
mess = np.array([1.498, 6.278, 5.46, 4.711,
3.893, 2.927, 2.188, 1.37])

p = (mess -theo) / theo

print(p)
