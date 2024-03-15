# kleinergauss.py

# Berechnet die Summe aller natürlichen Zahlen die kleiner oder gleich der Eingabe sind.

# Input:
#   n: int

# Output:
#   summe: float

# Narges, Nora 
# Version 1.0, 04.03.2024

# Userinput
n = int(input("Bitte eine Zahl eingeben: "))

# Variable für die Summe (wird schrittweise erhöht)
summe = 0

# Summe berechnen
for i in range(n+1):
    summe += i

# Ergebnis ausgeben
print("Die Summe der Zahlen ist ", summe)
