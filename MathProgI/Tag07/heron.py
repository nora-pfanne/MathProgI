'''
rationale_zahl.py

Narges, Nora
Version 1.0, 12.03.2024
'''

# Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import math

import sys
import importlib

# rationale_zahl aus einer vorherigen Aufgabe
sys.path.insert(1, './Tag07')
import rationale_zahl as rationale_zahl
importlib.reload(rationale_zahl) 

def heron(a, tol):

    global schritte

    # Startwert für k = 0
    x = a
    y = a / x
    
    # Ist die Tolerany erreicht?
    while (abs(x - y) >= tol):

        # Aufrufe zählen
        schritte += 1
    
        x = (x+y) / 2
        y = a / x

    return x


def heron_rational(a: rationale_zahl.Rationale_Zahl, tol: rationale_zahl.Rationale_Zahl):

    global schritte

    # Startwert für k = 0
    x = a
    y = a / x
    
    # Ist die Tolerany erreicht?
    while (abs(x.s * x.p / x.q) - (y.s * y.p / y.q)) >= (tol.s * tol.p / tol.q):

        # Aufrufe zählen
        schritte += 1
    
        x = (x+y) / rationale_zahl.Rationale_Zahl(1,2,1)
        y = a / x

    return x

#---------------------------------------------------
# Hauptprogramm

schritte = 0

x = []
y = []

A = 2

# (Läuft nur bis n = 15)
for i in range(16):

    # aktuelle Toleranz
    tol = 10 ** (-i)

    # Betrachte die Anzahl der Schritte
    heron_wert = heron(A,tol)
    print(heron_wert)
    x += [schritte]
    y += [abs(2 ** 0.5 - heron_wert) / 2 ** 0.5]
    schritte = 0


plt.loglog(x, y)
plt.title('Anzahl der Schritte')

plt.savefig('heron.png')
plt.cla()
plt.clf()

# Kovergenzgeschwindigkeit
q = math.log(abs((y[15] - y[11]) / (y[11] - y[5]))) / math.log(abs((y[11] - y[5]) / (y[5] - y[2])))
print("Kovergenzgeschwindigkeit:", q)


schritte = 0

A_rational = rationale_zahl.Rationale_Zahl(1,2,1)

x_rational = []
y_rational = []

# (Läuft nur bis n = 15)
for i in range(16):

    # aktuelle Toleranz
    tol_rational = rationale_zahl.Rationale_Zahl(1,1,10**i)

    # Betrachte die Anzahl der Schritte
    heron_wert = heron_rational(A_rational,tol_rational)
    x_rational += [schritte]
    y_rational += [abs(2 ** 0.5 - (heron_wert.s * heron_wert.p / heron_wert.q)) / 2 ** 0.5]
    print(y_rational[i])
    schritte = 0


plt.loglog(x_rational, y_rational)
plt.title('Anzahl der Schritte')

plt.savefig('heron_rational.png')
plt.cla()
plt.clf()

# Kovergenzgeschwindigkeit
q = math.log(abs((y_rational[6] - y_rational[3]) / (y_rational[3] - y_rational[1]))) / math.log(abs((y_rational[3] - y_rational[1]) / (y_rational[1] - y_rational[0])))
print("Kovergenzgeschwindigkeit:", q)
