'''
dreiecke.py

Dieses Programm zeichnet den Graphen einer gegebenen Funktion.


Eingabewerte:
    x1, y1, x2, m: int
    x0, y0, x1, m: int


Ausgabewerte: 
    Es wird eine Grafik für die jeweilige Teilaufgabe erzeugt und als png gespeichert.

Narges, Nora
Version 1.0, 07.03.2024
'''

# Bibliotheken
import matplotlib.pyplot as plt
import numpy as np

def zeichne_loglog_dreieck_U(x1, y1, x2, m):

    # gleiche Koordinaten
    x0 = x1
    y2 = y1 

    # Berechne y0
    y0 = np.exp(- m * (np.log(x2) - np.log(x0)) + np.log(y2))
    
    # Eckpunkte des Dreiecks
    eckpunkte = np.array([[x0, y0], [x1, y1], [x2, y2], [x0, y0]])
    
    # Koordinaten extrahieren
    x, y = eckpunkte[:, 0], eckpunkte[:, 1]
    

    # Plot erstellen
    plt.figure()
    plt.loglog(x, y, 'b-')
    plt.title('Dreieck (U)')
    plt.xlabel('X-Achse (log scale)')
    plt.ylabel('Y-Achse (log scale)')
    plt.grid(True)

    # Grafik speichern
    plt.savefig('dreieck_U.png')

def zeichne_loglog_dreieck_L(x0, y0, x1, m):
    
    # gleiche Koordinaten
    y1 = y0
    x2 = x1

    # Berechne y2
    y2 = np.exp(m * (np.log(x2) - np.log(x0)) + np.log(y0))
    
    # Eckpunkte des Dreiecks
    m = (np.log(y2) - np.log(y0)) / (np.log(x2) - np.log(x0))
    eckpunkte = np.array([[x0, y0], [x1, y1], [x2, y2], [x0, y0]])
    
    # Koordinaten extrahieren
    x, y = eckpunkte[:, 0], eckpunkte[:, 1]
    
    # Plot erstellen
    plt.figure()
    plt.loglog(x, y, 'b-')
    plt.title('Dreieck (L))')
    plt.xlabel('X-Achse (log scale)')
    plt.ylabel('Y-Achse (log scale)')
    plt.grid(True)
    
    # Grafik speichern
    plt.savefig('dreieck_L.png')


#---------------------------------------------------
# Hauptprogramm

'''
Konkave und konvexe Funktionen: Auf einem linearen Scale-Plot können konkave und konvexe Funktionen 
als gekrümmte Linien dargestellt werden, aber es kann schwierig sein, die Krümmung oder Steigung visuell zu bestimmen, 
insbesondere wenn die Funktion einen breiten Wertebereich hat. Auf einem logarithmischen Scale-Plot wird die Krümmung 
einer konkaven oder konvexen Funktion besser sichtbar, da die logarithmische Skala kleine Änderungen in den Daten 
stärker betont. Eine konkave Funktion wird auf einem logarithmischen Scale-Plot als Linie mit negativer Steigung 
erscheinen (da die Ableitung negativ ist), während eine konvexe Funktion als Linie mit positiver Steigung erscheinen 
wird (da die Ableitung positiv ist). Die visuelle Unterscheidung zwischen konkaven und konvexen Funktionen wird auf 
einem logarithmischen Scale-Plot deutlicher.
'''
# Funktion aufrufen
zeichne_loglog_dreieck_U(1,2,3,4)
zeichne_loglog_dreieck_L(1,2,3,4)