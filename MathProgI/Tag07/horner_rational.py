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

# hornerschema aus einer vorherigen Aufgabe
sys.path.insert(1, './Tag06')
import horner as hornerschema
importlib.reload(hornerschema) 


def taylor_arctan(x: rationale_zahl.Rationale_Zahl, n: int):

    # Koeffizienten für das Hornerschema
    a = []

    for k in range(n):

        # Bestimme die Koeffizienten
        a_k = rationale_zahl.Rationale_Zahl(1,1,1)

        if(k % 2):
            a_k = rationale_zahl.Rationale_Zahl(-1, 1, 2 * k + 1)
        else:
            a_k = rationale_zahl.Rationale_Zahl(1, 1, 2 * k + 1)

        a += [rationale_zahl.Rationale_Zahl(1, 0, 1), a_k]
    
    return a


def taylor_log(x: rationale_zahl.Rationale_Zahl, n: int):

    # Koeffizienten für das Hornerschema
    a = [rationale_zahl.Rationale_Zahl(1, 0, 1)]

    for k in range(1,n):

        # Bestimme die Koeffizienten
        a_k = rationale_zahl.Rationale_Zahl(1, 1, 1)

        if(k % 2):
            a_k = rationale_zahl.Rationale_Zahl(1, 1, k)
        else:
            a_k = rationale_zahl.Rationale_Zahl(-1, 1, k)

        a += [a_k]
    
    return a


def taylor_e(x: rationale_zahl.Rationale_Zahl, n: int):
     
     # Koeffizienten für das Hornerschema
    a = []

    for k in range(n):
        a_k = rationale_zahl.Rationale_Zahl(1, 1, math.factorial(k))
        a += [a_k]

    return a



# Approximation reeller Zahlen

testintervall = [2,4,6,8,10]


# e
y = []

# Generiere die Funktionswerte
for n in testintervall:
        x = rationale_zahl.Rationale_Zahl(1,1,1)
        a = taylor_e(x,n)
        y += [str(hornerschema.hornerschema(x,n,a))]

print("e:", y)



# Pi
y = []
# Generiere die Funktionswerte
for n in testintervall:
        x = rationale_zahl.Rationale_Zahl(1,1,1)
        vier = rationale_zahl.Rationale_Zahl(1,4,1)
        a = taylor_arctan(x, n)
        y += [str(vier * hornerschema.hornerschema(x,n,a))]

print("pi:", y)



# ln(2)
y = []
# Generiere die Funktionswerte
for n in testintervall:
        x = rationale_zahl.Rationale_Zahl(1,2,1)
        x_1 = rationale_zahl.Rationale_Zahl(1,1,1)
        a = taylor_log(x, n)
        y += [str(hornerschema.hornerschema(x_1, n, a))]

print("ln(2):", y)