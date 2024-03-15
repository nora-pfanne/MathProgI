'''
pi_kreis.py

Narges, Nora
Version 1.0, 13.03.2024
'''

# Bibliotheken
import sys
import importlib
import matplotlib.pyplot as plt
import numpy as np

# Punkte aus einer vorherigen Aufgabe
sys.path.insert(1, './Tag08')
import punkt as punkt
importlib.reload(punkt) 

def LKG(n: int):

    global x_0
    global a
    global b
    global m

    # Startwert von x ist x_0
    x = x_0

    # Liste mit Zufallszahlen
    zufallszahlen = [x]

    for i in range(n):

        # Bestimme x_n
        x = (a * x + b) % m

        # Ergänze die aktuelle Zahl
        zufallszahlen += [x]
    
    # x_0 überschreiben, damit beim nächsten Aufruf eine neue Liste generiert wird
    x_0 = x

    return zufallszahlen


def punkte_generieren(n):

    punkte = []

    global x_0
    global a
    global b
    global m
    # Zufallszahlen generieren
    x = LKG(n)
    y = LKG(n)

    for i in range(n):
        # Transformiere den Wert (Intervall [0;1])
        x[i] = x[i] / (m-1)

        # Transformiere den Wert (Intervall [0;1])
        y[i] = y[i] / (m-1)

        punkte += [punkt.Punkt(x[i],y[i])]
    
    return punkte


#----------------------------------------------------------------
# Hauptprogramm
    
a = 25173
b = 13849
m = 65536

x_0 = 42

# Anzahl der Punkte
anzahl_punkte = []
fehler = []

for exp in range(1,1000,10):

    n = exp
    anzahl_punkte += [n]

    punkte = punkte_generieren(n)
    ursprung = punkt.Punkt(0,0)

    # Zähler
    im_kreis = 0

    for i in range(n):
        if(ursprung.Abstand(punkte[i]) <= 1):
            plt.plot(punkte[i].X, punkte[i].Y, 'ro')
            im_kreis += 1
        else: 
            plt.plot(punkte[i].X, punkte[i].Y, 'ko')

    pi = 4*(im_kreis / n)

    # Fehler berechnen

    fehler_n = abs(np.pi - pi) / np.pi
    fehler += [fehler_n]



# Zeichne die Punkte in ein Koordinatensystem
plt.title('Pi approximieren')
plt.savefig('pi_approx.png')
plt.cla()
plt.clf()

# Fehler plotten
plt.loglog(anzahl_punkte, fehler)
plt.title('Pi approximieren')
plt.savefig('pi_approx_fehler.png')
plt.cla()
plt.clf()
