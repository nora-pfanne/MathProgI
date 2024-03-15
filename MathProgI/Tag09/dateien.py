'''
dateien.py

Narges, Nora
Version 1.0, 14.03.2024
'''
import numpy as np
import sys

# Kongruenzgenerator
def LKG(n: int):

    global x_0
    global a
    global b
    global m

    # Startwert von x ist x_0
    x = x_0

    # Liste mit Zufallszahlen
    zufallszahlen = [x]

    for i in range(n):

        # Bestimme x_n
        x = (a * x + b) % m

        # Ergänze die aktuelle Zahl
        zufallszahlen += [x]
    
    # x_0 überschreiben, damit beim nächsten Aufruf eine neue Liste generiert wird
    x_0 = x

    return zufallszahlen

#----------------------------------------------------------------
# Hauptprogramm
        

# globale Varibalen
a = 25173
b = 13849
m = 2 ** 16

# 100 Zahlen generieren
x_0 = 4
n = 100

zufallszahlen = LKG(n)

#----------------------------------------------------------------

# Zahlen zeilenweise in einer Datei abspeichern
g = open("zufallszahlen_1.txt","w")

header = "Erzeugt mit a = " + str(a) + " b =" + str(b) + " m = " + str(m) + " und x_0 = " + str(x_0) + "\n"
g.write(header)

for i in range(n):
    zeile = str(zufallszahlen[i] / (m-1)) + "\n"
    g.write(zeile)

g.close()

# Zeilenweise ausgeben
g = open("zufallszahlen_1.txt","r")
s = g.read()

# Header ausgeben
print(s.split("\n")[0])

# Zahlen ausgeben
for t in s.split("\n")[1:]:
    t = f"{t:{5}.{5}}"
    print(t)
g.close()

#----------------------------------------------------------------


# Zahlen (10 proi Zeile) in einer Datei abspeichern
g = open("zufallszahlen_2.csv","w")

g.write(header)

for i in range(0,n,10):
    
    for j in range(9):
        g.write("{y:4.3f}".format(y = zufallszahlen[i+j] / (m-1)) + ",")

    g.write("{y:4.3f}".format(y = zufallszahlen[10] / (m-1)))
    g.write("\n")

g.close()

# Zeilenweise ausgeben
g = open("zufallszahlen_2.csv","r")
s = g.read()

# Header ausgeben
print(s.split("\n")[0])

# Zahlen ausgeben
for t in s.split("\n")[1:]:
    print(t)
g.close()
