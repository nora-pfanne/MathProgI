'''
fibonacci.py

In diesem Programm werden die erste n Fibonacci-Zahlen rekursiv und iterativ berechnet.

Eingabewerte:
    n: int

Ausgabewerte: 
    fibonacci: Liste<int>
    

Narges, Nora
Version 1.0, 08.03.2024
'''

# Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import sys
import importlib

# ggT aus einer vorherigen Aufgabe
sys.path.insert(1, './Tag02')
import modularisierung as ggT
importlib.reload(ggT) 


# Globale Variable (Zähler)
zaehler = 0
zaehler_liste = []


def fibonacci(n: int):

    global zaehler
    global zaehler_liste

    # Leere Listen für die Fibonaccireihen
    fibonacci_rec_liste = []
    fibonacci_it_liste = []

    for i in range(n):

        # rekursie Variante
        fibonacci_rec_liste += [fibonacci_rec(i)]

        # Liste mit Aufrufzahlen aktualisieren
        zaehler_liste += [zaehler]
        zaehler = 0

        # iterative Variante
        fibonacci_it_liste += [fibonacci_it(i)]
    
    
    return [fibonacci_rec_liste, fibonacci_it_liste]


# Berechnet die nte Fibonaccizahl
def fibonacci_rec(n: int):

    
    # Abbruchbedingungen
    if(n == 0):
        return 0
    elif(n == 1):
        return 1

    # Rekursionsschritt
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_it(n: int):

    global zaehler

    # Liste mit n leeren Einträgen
    f = [0, 1]

    # Berechne schrittweise die nte Fibonaccizahl
    for i in range(2, n+1):
          # Für jeden Funktionsaufruf wird der Zähler erhöht
        zaehler += 1
        f += [f[i-1] + f[i-2]]
    
    return f[n]


def phi(n):

    # Formel für den goldenen Schnitt
    phi = abs((1 + 5 ** 0.5) / 2 - (fibonacci_it(n) / fibonacci_it(n-1))) / ((1 + 5 ** 0.5) / 2)

    return phi


#---------------------------------------------------
#---------------------------------------------------
# Hauptprogramm
        
# Test
n = 30

fibonaccireihe = fibonacci(n)

print('rekursiv:',fibonaccireihe[0])
print('iterativ:', fibonaccireihe[1])

# Betrachte die Anzahl der Aufrufe bei der rekursiven Variante
# Skalierung der Achsen
x = np.linspace(0, n, n)
y = zaehler_liste

# Achsen zeichnen und beschriften
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Anzahl der Aufrufe')

# Titel setzen
plt.title('Zähler')

# Speichere Grafik als png
plt.savefig('fibonacci_zaehler.png')

plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window

#---------------------------------------------------
# Goldener Schnitt
m = 50

# Skalierung der Achsen
x = np.linspace(2, m, m-2)

# y-Werte erzeugen
y = []
for i in range(2, m):
    y += [phi(i)]

# Achsen zeichnen und beschriften
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('phi')

# Titel setzen
plt.title('Goldener Schnitt')

# Speichere Grafik als png
plt.savefig('goldener_schnitt_plot.png')

# Achsen zeichnen und beschriften
plt.semilogy(x, y)
plt.xlabel('x')
plt.ylabel('phi')

# Titel setzen
plt.title('Goldener Schnitt')

# Speichere Grafik als png
plt.savefig('goldener_schnitt_semilogy.png')

# Achsen zeichnen und beschriften
plt.loglog(x, y)
plt.xlabel('x')
plt.ylabel('phi')

# Titel setzen
plt.title('Goldener Schnitt')

# Speichere Grafik als png
plt.savefig('goldener_schnitt_loglog.png')

#---------------------------------------------------
# ggT

fibonacci_ggT = []

k = 50

for i in range(2, k):
    fibonacci_ggT += [ggT.ggT1(fibonacci_it(n), fibonacci_it(n-1))]

print(fibonacci_ggT)
