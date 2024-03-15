'''
modularisierung.py

Modularisierte Variante für die ggT-Algorithmen mit Hauptprogramm

Eingabewerte:
    m: int
    n: int

Ausgabewerte: 
    ggT: int

Narges, Nora
Version 1.0, 05.03.2024
'''

def ggT1(m: int, n: int):

    # Bestimmung des ggT
    while (m != n):
        if(m > n):
            m -= n
        else:
            n -= m

    # Rückgabewert
    return m

def ggT2(m: int, n: int):

    # Varibale für den Rest der Division
    r = 0

    # Euklid - Algorithmus zur Berechnung des ggT
    while(n != 0):
        r = m % n
        m = n
        n = r

    # Rückgabewert
    return m

#---------------------------------------------------
# Hauptprogramm
'''
# Eingabe der Zahlen
m = int(input("m:"))
n = int(input("n:"))

# Prüfe, ob die Eingabe eine natürliche Zahl ist
if(m < 0 or n < 0):
    print("Keine natürliche Zahl!")
else:
    # Berechnung des ggT mit unterschiedlichen Algorithmen
    print("Der ggT ist", ggT1(m,n))
    print("Der ggT mit dem Euklid-Algorithmus ist", ggT2(m,n))
'''