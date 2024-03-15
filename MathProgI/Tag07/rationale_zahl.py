'''
rationale_zahl.py

Narges, Nora
Version 1.0, 12.03.2024
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

class Rationale_Zahl:

    # Initialisierung der Klasse 
    def __init__(self, s: int, p: int, q: int):
        
        # Definition der Attribute
        if(p < 0 or q <= 0):
            print("p >= 0 und q > 0 müssen natürliche Zahlen sein!")
            pass
        
        # p und q sollen teilerfremd sein
        elif (ggT.ggT2(p, q) != 1):

            # durch ggT teilen
            self.p = p // ggT.ggT1(p, q)
            self.q = q // ggT.ggT1(p, q)
            self.s = s

        else:
            self.p = p
            self.q = q
            self.s = s


    # Ausgabe definieren
    def __str__(self):

        # besondere Darstellungen (Ganze Zahlen)
        if(self.p == 0):
            return "%s"%(self.p)
        
        elif(self.q == 1):
            return "%s"%(self.s * self.p)
        
        else:
            return "%s/%s"%(self.s * self.p, self.q)
    

    # Operatoren überladen
    def __add__(self, other):
        
        # Ergebnis
        ergebnis = Rationale_Zahl(1, 1, 1)
        zaehler1 = 1
        zaehler2 = 1
        nenner = 1

        # Brüche gleichnamig?
        if(self.q != other.q):

            # Brüche gleichnamig machen und erweitern
            nenner = self.q * other.q
            zaehler1 = self.p * other.q
            zaehler2 = other.p * self.q

        else:
            nenner = self.q
            zaehler1 = self.p
            zaehler2 = other.p
            
        # Zähler berechnen
        zaehler = self.s * zaehler1 + other.s * zaehler2
        
        # Attribute des Ergebnisses anpassen
        ergebnis.q = nenner
        ergebnis.p = abs(zaehler)

        if(zaehler < 0):
            ergebnis.s = -1
        else:
            ergebnis.s = 1

        return ergebnis


    def __sub__(self, other):

        # Addition mit negativem 2. Summanden
        if(other.s == 1):
             negativ = Rationale_Zahl(-1, other.p, other.q)
            
        else:
            negativ = Rationale_Zahl(1, other.p, other.q)
        
        return self + negativ
    

    def __mul__(self, other):

        # Zähler und Nenner multiplizieren
        p = self.p * other.p
        q = self.q * other.q
        s = self.s * other.s

        # Ergebnis
        ergebnis = Rationale_Zahl(s,p,q)

        return ergebnis
        

    def __truediv__(self, other):
        
        # Zähler ist 0
        if(self.p == 0 or other.p == 0):
            return Rationale_Zahl(1, 0, 1)
        
        # mit dem Kehrwert multiplizieren
        else: 
            kehrwert = Rationale_Zahl(other.s, other.q, other.p)
            return self * kehrwert

        

#---------------------------------------------------
# Hauptprogramm

'''
bruch1 = Rationale_Zahl(1,1,1)
print(bruch1)

bruch2 = Rationale_Zahl(-1,2,3)
print(bruch2)

# Operatoren testen
print(bruch1, "+", bruch2, "=", bruch1 + bruch2)
print(bruch1, "-", bruch2, "=", bruch1 - bruch2)
print(bruch1, "*", bruch2, "=", bruch1 * bruch2)
print(bruch1, ":", bruch2, "=", bruch1 / bruch2)'''