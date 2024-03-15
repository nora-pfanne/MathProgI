# planetenperioden.py

# Berechnet die Umlaufzeiten der Planeten und gibt diese zusammen mit dem Planetennamen und 
# der Entfernung zur Sonne aus.

# Input:
#   planeten: Liste<String>
#   halbachsen: Liste<float>

# Output:
#   Planet: String
#   Halbachse: float
#   Umlaufzeit: float

# Narges, Nora 
# Version 1.0, 04.03.2024

# Listen mit Planeten und Halbachsen
planeten = ["Merkur", "Venus", "Erde", "Mars", "Juppiter", "Saturn", "Uranus", "Neptun"]
halbachsen = [0.39, 0.72, 1.0, 1.52, 5.2, 9.54, 19.18, 30.06]

# Leere Liste für die Umlaufzeiten
umlaufzeiten = list(range(8))

# Umlaufzeiten berechnen
for i in range(len(planeten)):

    # 3. Kepler'sches Gesetz: T^2 / t^3 = C
    umlaufzeiten[i] = (halbachsen[i] ** 3) ** 0.5

    # Ausgabe der Ergebnisse
    print("Planet ", planeten[i], " hat eine Entfernung von ", halbachsen[i], " zur Sonne und hat eine Umlaufzeit von ",  umlaufzeiten[i], " Jahren") 
