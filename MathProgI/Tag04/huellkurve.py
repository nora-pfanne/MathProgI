'''
huellkurve.py

Dieses Programm verteilt auf dem Einheitskreis n Punkte Pi := (cos(αi ), sin(αi )) gleichmäßig 
und verbindet für i = 1, 2, . . . , n den Punkt Pi mit Qi := (− cos(3 αi ), − sin(3 αi )) 
mit einer Linie.
Danach wird allgemeiner Qi := (− cos(k αi ), − sin(k αi )) betrachtet mit unterschiedlichen 
Werten für k.

Eingabewerte:
    n: int
    k: int

Ausgabewerte: 
    Es wird eine Grafik erzeugt und als png gespeichert.

Narges, Nora
Version 1.0, 07.03.2024
'''

# Bibliotheken
import matplotlib.pyplot as plt
import numpy as np


def kreis(n: int):

    # Variante 1: k = 3
    # Achsen definieren und zeichnen
    fig, achsen = plt.subplots()
    achsen.set_aspect('equal')

    # Kreis zeichnen (indem Punkte auf dem Einheitskreis berechnet werden)
    theta = np.linspace(0, 2*np.pi, 100)
    achsen.plot(np.cos(theta), np.sin(theta), color='b')

    # Berechne und zeichne die Punkte Pi und Qi
    alpha = np.linspace(0, 2*np.pi, n, endpoint=False)
    for a in alpha:
        Pi = (np.cos(a), np.sin(a))
        Qi = (-np.cos(3*a), -np.sin(3*a))
        achsen.plot([Pi[0], Qi[0]], [Pi[1], Qi[1]], color='r')

    # Speichere Grafik als png
    plt.savefig('kaustik.png')


def kreis_k(n: int):

    '''
    Bei der Wahl von k beeinflusst die Anzahl der Reflexionen die Form der Kaustik. 
    Für größere Werte von k (d. h. mehr Reflexionen) wird die Kaustik komplexer und dichter. 
    '''

    # Variante 2: k beliebig
    # Setze unterschiedliche Werte für k ein und zeichne jeweils eine Kaustik
    fig, achsen = plt.subplots(2, 2)
    fig.suptitle('Kaustik für verschiedene k')

    for k in range(1,5):

        # Erstelle jeweils einen Subplot
        ax = achsen[(k-1) // 2, (k-1) % 2]

        # Kreis zeichnen (indem Punkte auf dem Einheitskreis berechnet werden)
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(np.cos(theta), np.sin(theta), color='b')

        # Berechne und zeichne die Punkte Pi und Qi
        alpha = np.linspace(0, 2*np.pi, n, endpoint=False)
        for a in alpha:
            Pi = (np.cos(a), np.sin(a))
            Qi = (-np.cos(k*a), -np.sin(k*a))
            ax.plot([Pi[0], Qi[0]], [Pi[1], Qi[1]], color='r')

        # Titel hinzufügen
        ax.set_title('k = ' + str(k))

    # Grafiken anordnen
    plt.tight_layout()

    # Speichere Grafik als png
    plt.savefig('kaustik_k.png')


#---------------------------------------------------
# Hauptprogramm

# Usereingaben
anzahl_punkte = int(input("Gebe die Anzahl der Punkte ein:"))

# Zeichne die Kaustik für eine eingegebene Anzahl an Punkten
kreis = kreis(anzahl_punkte)
kreis_k = kreis_k(anzahl_punkte)
