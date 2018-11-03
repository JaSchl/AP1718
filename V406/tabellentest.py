#Das sind die beiden packages, die du laden musst
import numpy as np
from astropy.io import ascii

#Hier sagst du ihm aus welcher Datei er die Messwerte bekommt
# Das beispiel ist aus dem Beugungsversuch A ist der Abstand und I der Strom
# kannst sie aber auch x und y nennen ist völlig egal
A, I = np.genfromtxt('mess15.txt', unpack=True)

# hiermit wird nun die Tabelle erstellt.
# Die bezeichnungen von A und I müssen mit dem Oben übereinstimmen
#Hier sind jetzt drei Spalten. Einmal Abstand, Strom und der Strom mit dem Abgezogenen Dunkelstrom von 5nA
#Mit einem weiteren Komma fügst du eine neue Spalte ein.
ascii.write([A, I, I-5], 'einzeltab.tex', format='latex')
