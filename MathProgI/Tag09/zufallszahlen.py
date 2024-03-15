'''
zufallszahlen.py

Narges, Nora
Version 1.0, 14.03.2024
'''
import numpy as np
import matplotlib.pyplot as plt

g = open("Tag09/Zufallszahlen.txt","r")

s = True

zahlen = []

# erste Zeile lesen, aber direkt überschreiben
s = g.readline()

# Zeile einlesen
while s:

    # Zeichen entfernen
    s = g.readline().replace("\n","")
    
    if(s):
        # einzelne Zahlen auslesen
        for t in s.split(","):
            zahlen += [float(t)]

g.close()

# Erwartungswert
mu = sum(zahlen) / len(zahlen)

# Standardabweichung
sigma = np.std(zahlen)
    
# Normalverteilung
y = []
for x in zahlen:
    y += [(1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (((x -mu) / sigma) ** 2))]



# Histogramm
plt.hist(zahlen, 200, density=True)
plt.plot(zahlen, y, 'r*')
plt.savefig('histogramm.png')
plt.cla()
plt.clf()