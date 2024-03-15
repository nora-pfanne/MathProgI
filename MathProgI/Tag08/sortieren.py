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


def median(ell, i, j, k):
      
      if(((ell[j] < ell[i]) and (ell[i] <= ell[k])) or ((ell[k] < ell[i]) and (ell[i] < ell[j]))):
        return i
      elif(((ell[j] < ell[k]) and (ell[k] <= ell[i])) or ((ell[i] < ell[k]) and (ell[k] < ell[j]))):
        return k
      else:
        return j
      

def insertionsort(ell: list):

    for i in range(1,len(ell)):

        # Startwert
        x = ell[i]

        j = i
        
        while((j > 0) and (x < ell[j-1])):

            ell[j] = ell[j-1]
            j -= 1
    
        ell[j] = x



def quicksort_helper(ell, start, ende):
     
    i = median(ell, start, ende, start + (ende-start) // 2)

    ell[i], ell[ende] = ell[ende], ell[i]
    
    pivot = ell[ende]

	# Zeige an, wo die sortierte Liste endet
    listenende = start - 1

    # Finde alle Elemente, die kleiner als pivot sind
    for j in range(start, ende):
        if ell[j] <= pivot:

			# Zahl ist kleiner als pivot
            listenende += 1

            ell[listenende], ell[j] = ell[j], ell[listenende]

	# Setze pivot in die Mitte und wähle ein neues pivot-Element
    ell[listenende + 1], ell[ende] = ell[ende], ell[listenende + 1]

	# Gebe zurück, wo das pivot-Element ist
    return listenende + 1



def quicksort(ell, start, ende):

	if(start < ende):

		# Finde das pivot-Element
		pivot = quicksort_helper(ell, start, ende)

		# linker Teil
		quicksort(ell, start, pivot - 1)

		# Recursive call on the right of pivot
		quicksort(ell, pivot + 1, ende)


#----------------------------------------------------------------
# Hauptprogramm

a = 25173
b = 13849
m = 45

x_0 = 32

# Dauer je n tracken
anzahl = []
zeiten_insertion = []
zeiten_quick = []

for exp in range(1,1000,10):

    n = exp
    anzahl += [n]

    ell_insertion = LKG(n)
    kopie = ell_insertion

    # Messe die Zeit
    start = time.time()
    insertionsort(ell_insertion)
    ende = time.time()

    zeiten_insertion += [ende-start]

    print(all(ell_insertion[i] <= ell_insertion[i+1] for i in range(len(ell_insertion) - 1)))

    #print(kopie.sort() == ell_insertion)
    #print(kopie)
    #print(ell_insertion)

    ell_quick = LKG(n)
    kopie2= ell_quick

    start = time.time()
    quicksort(ell_quick, 0, len(ell_quick)-1)
    ende = time.time()

    #print(kopie2.sort() == ell_quick)
    #print(kopie2)
    #print(ell_quick)

    zeiten_quick += [ende-start]


plt.loglog(anzahl, zeiten_insertion)
plt.loglog(anzahl, zeiten_quick)
plt.savefig('zeiten.jpeg')

plt.cla()
plt.clf()
