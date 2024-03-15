'''
rekursion.py

Rekursive Varianten der ggT-Algorithmen

Eingabewerte:
    m: int
    n: int

Ausgabewerte: 
    ggT: int

Narges, Nora
Version 1.0, 05.03.2024
'''

def ggT1_rec(m: int,n: int):

    # Abbruchbedingung
    if(m == n):
        return m
    
    # Rekusionsschritt
    elif(m > n):
        return ggT1_rec(m-n,n)
    else:
        return ggT1_rec(m,n-m)


def ggT2_rec(m: int,n: int):

    # Abbruchbedingung
    if(n == 0):
        return m
    
    # Rekusionsschritt
    else: 
        return ggT2_rec(n, m%n)
    

#---------------------------------------------------
# Hauptprogramm

# Eingabe der Zahlen
m = int(input("m:"))
n = int(input("n:"))

# Prüfe, ob die Eingabe eine natürliche Zahl ist
if(m < 0 or n < 0):
    print("Keine natürliche Zahl!")
else:
    # Berechnung des ggT mit unterschiedlichen Algorithmen
    print("Der ggT ist", ggT1_rec(m,n))
    print("Der ggT mit dem Euklid-Algorithmus ist", ggT2_rec(m,n))
