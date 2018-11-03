import numpy as np

R = 509.5
R1 = 221.84
C = 2.098*10**-9
L = 10.11*10**-3


nu, dt, phi, phir = np.genfromtxt("Messwerte/Mess3.txt", unpack = True, skip_header = 3)
nu = nu*10**3
dt = dt*10**-6

Uc = 1 / (np.sqrt((1-L*C*nu**2)**2 + nu**2 * R**2 * C**2))
f = np.arctan(-(nu * R * C) / (1 - (nu**2 * L * C)))
phirad2 = 2*np.pi*f*dt
phirad = 2*np.pi*nu*dt
om = np.sqrt(((1)/(L*C)) - ((R1**2) / (2*L**2)))
om1 = R/(2*L) + np.sqrt(((R**2)/(4*L**2))+((1)/(L*C)))
om2 = -R/(2*L) + np.sqrt(((R**2)/(4*L**2))+((1)/(L*C)))

v, U, UcU0= np.genfromtxt("Messwerte/Mess2.txt", unpack = True, skip_header = 3)
U0 = 6.8
Uc2 = 1 / (np.sqrt((1-L*C*v**2)**2 + v**2 * R**2 * C**2))



print(Uc)
print(f)
print(phirad2)
print(phirad)
#print(U/U0)
print((om)/(2*np.pi))
print((om1)/(2*np.pi))
print((om2)/(2*np.pi))
