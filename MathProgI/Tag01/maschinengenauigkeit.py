# maschinengenauigkeit.py

# Berechnet die Maschinengenauigkeit mit der entsprechenden Mantisse von Gleitkommazahlen.

# Input:
#   m: int

# Output:
#   m: int
#   eps: float

# Narges, Nora 
# Version 1.0, 04.03.2024

# Probiere unterschiedliche Längen für die Mantisse (64-Bit Zahlen)
for m in range(65):
    # kleinste Zahl > 1
    kleinste = 1 + 2 ** (-m)

    # Berechne die Genauigkeit und gebe das Ergebnis aus
    print("Für die Mantisse", m, "ist die Genauigkeit", kleinste-1) # m = 52, a = 11

# Maschinengenauigkeit
m = 52
eps = (1 + 2 ** (-m)) - 1
print("Die Maschinengenauigkeit ist", eps, "für die Mantisse", m)
