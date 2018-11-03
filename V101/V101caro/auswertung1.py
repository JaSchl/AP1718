import numpy as np
from scipy.stats import sem
from uncertainties import ufloat
import uncertainties.unumpy as unp

Kräfte = np.genfromtxt("messung1.tex", unpack = False)
Kräfte = Kräfte.T
Winkel = np.array([40, 90, 135, 180, 225, 250, 270, 300, 315, 360])
Auslenkung = np.array([0.22, 0.29, 0.40, 0.50, 0.60, 0.62, 0.63, 0.74, 0.74, 0.78])

#WRG1 = np.array([n*Längen[0]/Winkel[i] for i, n in enumerate(Kräfte[0]) ])
#WRG2 = np.array([n*Längen[1]/Winkel[i] for i, n in enumerate(Kräfte[1]) ])
#WRG3 = np.array([n*Längen[2]/Winkel[i] for i, n in enumerate(Kräfte[2]) ])

#WRG = np.concatenate([WRG1, WRG2, WRG3])
#Mittelwert = np.mean(WRG)

Fehler = np.std(WRG, ddof = 1)
s = 1/np.sqrt(len(WRG))
Fehler = s*Fehler
Null = 0000

WF = np.array([Mittelwert, Fehler, Null, Null])

print(WRG)
print(Mittelwert)
print(Fehler)
np.savetxt("WRGstat.txt", np.column_stack([WRG1, WRG2, WRG3, WF]), header = "10 cm, 15 cm, 20 cm, Wert und Fehler untereinander")
