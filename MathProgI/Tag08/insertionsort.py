'''
insertionsort.py

Narges, Nora
Version 1.0, 13.03.2024
'''
import time
import matplotlib.pyplot as plt

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



def insertionsort(ell: list):

    # Startwert
    x = ell[0]

    for i in range(1,len(ell)):
        
        if(x > ell[i]):

            for j in range(i,0,-1):

                if(ell[j] < ell[j-1]):
                    ell[j], ell[j-1] = ell[j-1], ell[j]
                else:
                    pass

        x = ell[i]
    
    return ell


def quicksort(ell):

    pivot = 0
    start = 1
    ende = len(ell)-1

    sort = quicksort_helper(start, ende, pivot, ell)


def quicksort_helper(start, ende, pivot, ell):
        
    # Sortiere in zwei Listenteile
    while(start <= ende):

        print(ell)
        print(ell[pivot])
        print(pivot)
        print(start)

        if(ell[pivot] >= ell[start]):
            
            for i in range(start, pivot, -1):
                ell[i-1], ell[i] = ell[i], ell[i-1]

            pivot += 1
        
        start += 1
        
    # Quicksort bei den Teilliisten
    if(pivot <= len(ell)-1):
        #teil1 = quicksort_helper(pivot+2, len(ell)-1, pivot+1, ell)
        teil2 = quicksort_helper(1, pivot+1, 0, ell)


#----------------------------------------------------------------
# Hauptprogramm

a = 25173
b = 13849
m = 45

x_0 = 32

# Dauer je n tracken
anzahl = []
zeiten = []

for exp in range(1,3):

    n = 10 ** exp
    anzahl += [n]

    ell = LKG(n)
    print(ell)

    

    # Messe die Zeit
    start = time.time()
    sortiert = insertionsort(ell)
    ende = time.time()
    zeiten += [ende-start]

    print(ell.sort() == sortiert)

    #sortiert = quicksort(ell)
    #print(ell)

print(zeiten)

plt.plot(anzahl, zeiten)
plt.savefig('zeiten.jpeg')

plt.cla()
plt.clf()
