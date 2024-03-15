'''
ggT.py

Berechnet den ggT zweier Zahlen

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

# Bestimmung des ggT
while (m != n):
    if(m > n):
        m -= n
    else:
        n -= m

# Ausgabe
print("Der ggT ist", m)
