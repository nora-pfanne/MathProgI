'''
collatz.py

Dieses Programm implementiert die Collatz-Vermutung auf 4 Weisen:
- Ex1: rekursiv
- Ex2: iterativ
- Ex3: rekursiv, bricht beim Zyklus (4,2,1) ab
- Ex4: Berechen die Anzahl der Folgenglieder, bis der Zyklus (4,2,1) erreicht ist


Eingabewerte:
    wort: str
    wort2: str

Ausgabewerte: 
    Palindrom?: boolean
    Annagramm?: boolean
    Isogramm?: boolean

Narges, Nora
Version 1.0, 06.03.2024
'''
# Import von Bibliotheken
import matplotlib.pyplot as plt


def plotten(ywerte):
    
    x = []
    # Auf der x-Achse sollen die Werte von 0 - 49 stehen
    for i in range(len(ywerte)):
        x += [i]

    # Auf der y-Achse werden die Reihenglieder zugeordnet
    y = ywerte

    plt.plot(x,y,'b o') # plotten von x gegen y

    # Achsenbeschriftung
    plt.xlabel('x') 
    plt.ylabel('y')

    plt.title('Experiment') # Titel der Grafik

    plt.show() # Grafik anzeigen


def experiment1(a: int):

    # Gebe die entstandene Reihe aus
    return experiment1reihe([a], 50)



def experiment1reihe(reihe, counter):

    # Abbruchbedungung:
    # Wir haben 50 Elemente berechnet
    if (counter == 1):
        return reihe
    
    else:
        # Aktuelles a ist eine gerade Zahl
        if(reihe[-1] % 2 == 0):
            counter -= 1
            return experiment1reihe(reihe + [reihe[-1] // 2], counter)
        
        # Aktuelles a ist eine ungerade Zahl
        else:
            counter -= 1
            return experiment1reihe(reihe + [3 * reihe[-1] + 1], counter)


def experiment2(a: int):

    # Lege eine Liste an, die bereits den Startwert enthält
    reihe = [a]

    # Berechne schrittweise die restlichen Folgenglieder
    for i in range(49):
        
        # Aktuelles a ist eine gerade Zahl
        if(reihe[-1] % 2 == 0):
            reihe = reihe + [reihe[-1] // 2]
        
        # Aktuelles a ist eine ungerade Zahl
        else:
            reihe = reihe + [3 * reihe[-1] + 1]
    
    return reihe



def experiment3(a: int):

    # Lege eine Liste an, die bereits den Startwert enthält
    reihe = [a]

    # Berechne schrittweise die restlichen Folgenglieder
    for i in range(49):

        if(len(reihe) >= 3):
            if(reihe[-1] == 1 and reihe[-2] == 2 and reihe[-3] == 4):
                break
        
        # Aktuelles a ist eine gerade Zahl
        if(reihe[-1] % 2 == 0):
            reihe = reihe + [reihe[-1] // 2]
        
        # Aktuelles a ist eine ungerade Zahl
        else:
            reihe = reihe + [3 * reihe[-1] + 1]
    
    return reihe


def experiment4(a: int):

    # Berechne die Anzahl der Folgenglieder der abgebrochenen Reihe
    return len(experiment3(a)) - 3 


def experiment5(m: int):

    # Leere Liste für die Pfadlängen
    pfad = []

    # Probiere unterschiedliche Werte für a
    for a in range(m):
        pfad += [experiment4(a)]

    return pfad


#---------------------------------------------------
# Hauptprogramm
        
input = int(input("Gebe einen Startwert ein:"))

# Ergebnisse aus den Experimenten
reihe_rec = experiment1(input)
reihe_it = experiment2(input)
abgebrochenereihe = experiment3(input)
anzahlglieder = experiment4(input)
pfadlänge = experiment5(500)

print(reihe_rec)
print(reihe_it)
print(abgebrochenereihe)
print(anzahlglieder)
print(pfadlänge)

# Plot
plotten(reihe_it)
plotten(pfadlänge)
   