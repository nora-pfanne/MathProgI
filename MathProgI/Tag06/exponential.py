'''
exponential.py

In diesem Programm werden Ansätze zur Berechnung der Exponentialfunktion in Hinblick
auf ihre Effizienz verglichen.
    

Narges, Nora
Version 1.0, 11.03.2024
'''

# Bibliotheke
import matplotlib.pyplot as plt
import math
import numpy as np

'''
Berechnung der Exponentialfunktion mit dem Hornerschema an der Stelle x, 
abgeschätzt bis zum n-ten Reihenglied.

Eingabe:
    x: float
    n: int

Ausgabe:
    y: float
'''
def e_n(x, n: int):
    
    b = a(n)
    
    while(n != 0):

        b = a(n-1) + x * b
        n -= 1

    return b 

    
def a(n):
    return 1.0 / math.factorial(n)


'''
Funktion aus der Aufgabenstellung

Eingabe:
    x: float
    n: int

Ausgabe:
    y: float
'''
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


'''
Funktion aus der Aufgabenstellung mit veränderter

Eingabe:
    x: float
    n: int

Ausgabe:
    y: float
'''
def exponentialfunktion_neu(x, n):

    if x < 0.0:
        return 1.0 / exponentialfunktion_neu(-x, n)

    elif x >= 0.25:
        tmp = exponentialfunktion_neu(x/2.0, n)
        return tmp * tmp

    else:
        # Berechnung von e_n(x)
        y = e_n(x,n)
        return y
    
#---------------------------------------------------
# Hauptprogramm
print(exponentialfunktion(1, 100))


# Intervall abtasten
testintervall = np.arange(-1.5,2.5,0.01).tolist()


for n in range(2,11,2):
        
        # Skalierung der Achsen
        y = []
        
        # Generiere die Funktionswerte
        for x in testintervall:
             y += [exponentialfunktion(x,n)]

        # Subplot:
        plt.subplot(2, 3, n//2)
        plt.semilogy(testintervall, y)
        plt.xlabel('x')
        plt.ylabel('y')

        # Titel setzen
        plt.title(n)

# Speichere Grafik als png
plt.tight_layout()


# Vergleich von e_2(x) und e(x)

# Skalierung der Achsen (nur für n = 2)
y = []
y_2 = []

# Generiere die Funktionswerte
for x in testintervall:
        y += [math.exp(x)]
        y_2 += [exponentialfunktion(x,2)]

plt.subplot(2, 3, 6)
plt.semilogy(testintervall, y)
plt.semilogy(testintervall, y_2)
plt.title('Vergleich')
plt.savefig('exponentialfunktion.png')
plt.cla()
plt.clf()

'''
Für n > 2 weicht die Gerade kaum von der der e-Funktion ab.
'''

# Relativer Fehler

fehler = []

# Relativen Fehler berechnen
for x in testintervall:
     fehler += [abs(math.exp(x) - exponentialfunktion(x,10)) / math.exp(x)]

plt.semilogy(testintervall, fehler)
plt.title('Relativer Fehler')

plt.savefig('fehler.png')
plt.cla()
plt.clf()




# Auswertungsstrategie x < 0.25
fehler = []

# Relativen Fehler berechnen
for x in testintervall:
     fehler += [abs(math.exp(x) - exponentialfunktion_neu(x,10)) / math.exp(x)]

plt.plot(testintervall, fehler)
plt.title('Relativer Fehler')
plt.savefig('fehler_neu.png')
plt.cla()
plt.clf()




print("e ist ungefähr:", e_n(1, 100))

testintervall = np.arange(0,100,1).tolist()


y = []

# Generiere die Funktionswerte
for n in testintervall:
        y += [abs(math.exp(1) - exponentialfunktion(1,n)) / math.exp(1)]

plt.semilogy(testintervall, y)
plt.title('e approximieren')
plt.savefig('e.png')
plt.cla()
plt.clf()
