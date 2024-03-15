'''
teilenmitrest.py

Berechnet den ggT zweier Zahlen mit dem Euklid-Algorithmus

Eingabewerte:
    m: int
    n: int

Ausgabewerte: 
    ggT: int

Narges, Nora
Version 1.0, 05.03.2024
'''

# Eingabe der Zahlen
m = int(input("m:"))
n = int(input("n:"))

# Varibale für den Rest der Division
r = m % n

# Euklid - Algorithmus zur Berechnung des ggT
while(r != 0):
    # m = alpha * n + r
    r = m % n
    m = n
    n = r
    
# Ausgabe
print("Der ggT ist", m)
