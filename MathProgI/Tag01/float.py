# float.py

# Berechnet die Exponentenlänge und dazugehörige größte darstellbare Zahl

# Input:
#   eps: float

# Output: 
#   groesste: float

# Narges, Nora 
# Version 1.0, 04.03.2024

# Maschinengenauigkeit aus der letzen Aufgabe
eps = (1 + 2 ** (-52)) - 1
print(eps)

# Probiere unterschiedliche Längen für die Exponentenlänge (64-Bit Zahlen)
for a in range(12):
    groesste = 2 ** (2 ** (a-1) -1) * (2 - eps)
    print("Für die Exponentenlänge ", a, " ist die Zahl ", groesste) # a = 11, danach ist die Darstellung nicht möglich

# Größte Zahl:
groesste = 2 ** (2 ** (11-1) -1) * (2 - eps)   
print("Die größte Zahl ist ", groesste, " mit der Exponentenlänge ", 11)
