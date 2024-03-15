'''
generator.py

Narges, Nora
Version 1.0, 13.03.2024
'''

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


def periode(zufallszahlen: list):

    # Startwert
    x = zufallszahlen[0]

    # Index
    i = 1

    while((i < len(zufallszahlen)-1) and (x != zufallszahlen[i])):
        i += 1
    
    return i


#----------------------------------------------------------------
# Hauptprogramm
        

# globale Varibalen
a = 7
b = 4
m = 15

# Test 1
x_0 = 4
zufallszahlen = LKG(20)
print(zufallszahlen)
print('Periode:', periode(zufallszahlen))

zufallszahlen = LKG(20)
print(zufallszahlen)
print('Periode:', periode(zufallszahlen))

# Test 2
x_0 = 11
zufallszahlen = LKG(20)
print(zufallszahlen)
print('Periode:', periode(zufallszahlen))

# Test mit Knuth-Zahlen
a = 25173
b = 13849
m = 65536
zufallszahlen = LKG(20)
print(zufallszahlen)
print('Periode:', periode(zufallszahlen))
