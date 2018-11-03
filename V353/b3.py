import matplotlib.pyplot as plt
import numpy as np

U = 21.59140294
RC = 0.05926156
x,y,a = np.genfromtxt('Messwerte/b.txt', unpack=True)
b = 1000/x
z = a/b * 2*np.pi
z_plt = np.linspace(0, 2)

plt.polar(z, y/U, 'rx')
plt.polar(z_plt, np.cos(z_plt), 'k-')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/b3.pdf')
