# modkleinergauss.py

# Berechnet die Summe aller positiven Zahlen, die kleiner oder gleich der Eingabe sind (Schrittweite 0.5).

# Input:
#   n: int

# Output:
#   summe: float

# Narges, Nora 
# Version 1.0, 04.03.2024

import sys

# Userinput
n = int(sys.argv[1])

# Variable für die Summe (wird schrittweise erhöht)
summe = 0

# Schrittweise Berechnung der Summe
for i in range(1, n+1):
    summe += i + (i-1) + 0.5


# Ergebnis ausgeben
print("Die Summe der Zahlen ist ", summe)
