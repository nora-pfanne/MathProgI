'''
partialsumme.py

In diesem Programm werden Ansätze zur Berechnung der Exponentialfunktion in Hinblick
auf ihre Effizienz verglichen.
    

Narges, Nora
Version 1.0, 11.03.2024
'''

# Bibliotheke
import matplotlib.pyplot as plt
import math
import numpy as np

def partialsumme(x, n: int):

    y = 0

    for i in range(n):

        y += (x ** i / math.factorial(i))

    return y

def kleinstes_m(x):

    n = 0

    while(partialsumme(x,n) != partialsumme(x,n+1)):
        n +=1
    
    return n


def e_n(x, n: int):
    
    b = a(n)
    
    while(n != 0):

        b = a(n-1) + x * b
        n -= 1

    return b 

    
def a(n):
    return 1.0 / math.factorial(n)

def exponentialfunktion(x, n):

    if x < 0.0:
        return 1.0 / exponentialfunktion(-x, n)

    elif x >= 1.0:
        tmp = exponentialfunktion(x/2.0, n)
        return tmp * tmp

    else:
        # Berechnung von e_n(x)
        y = e_n(x,n)
        return y



def kleinstes_m_horner(x):

    n = 0

    while(exponentialfunktion(x,n) != exponentialfunktion(x,n+1)):
        n +=1
    
    return n


#---------------------------------------------------
# Hauptprogramm

testintervall = np.arange(-1.5,2.5,0.01).tolist()

# y-Werte
y = []
y_horner = []

for x in testintervall:
     y += [kleinstes_m(x)]
     y_horner += [kleinstes_m_horner(x)]

plt.plot(testintervall, y)
plt.plot(testintervall, y_horner)
plt.title('Kleinstes m')

plt.savefig('kleinstes_m.png')
plt.cla()
plt.clf()
