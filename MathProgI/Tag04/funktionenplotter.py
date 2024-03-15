'''
funktionenplotter.py

Dieses Programm zeichnet den Graphen einer gegebenen Funktion.


Eingabewerte:
    teilaufgabe: int

Ausgabewerte: 
    Es wird eine Grafik für die jeweilige Teilaufgabe erzeugt und als png gespeichert.

Narges, Nora
Version 1.0, 07.03.2024
'''

# Bibliotheken
import matplotlib.pyplot as plt
import numpy as np

def funktion_plotten(teilaufgabe):
    
    # Je nachdem, welche Funktion gezeichnet werden soll, wird die entsprechende Teilaufgabe /
    # Funktionsgleichung(en) ausgewählt

    if teilaufgabe == 'a':

        # Skalierung der Achsen
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)

        # Achsen zeichnen und beschriften
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')

        # Titel setzen
        plt.title('f(x) = sin(x)')

        # Speichere Grafik als png
        plt.savefig('sin_x_plot.png')

    elif teilaufgabe == 'b':

        # Skalierung der Achsen
        x = np.linspace(-2, 2, 100)
        y = ((4 - x**2) ** 0.5)

        # Achsen zeichnen und beschriften
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')

        # Titel setzen
        plt.title('f(x) = sqrt(4 - x^2)')

        # Speichere Grafik als png
        plt.savefig('sqrt_4_x2_plot.png')

    elif teilaufgabe == 'c':

        # Da in dieser Teilaufgabe mehrere Funktionsgraphen gezeichnet werden sollen
        # wird "subplot" verwendet 

        # x-Werte
        x = np.linspace(0, 100, 100)

        # Funktionsgleichungen
        f1 = np.exp(x)
        f2 = x + 1
        f3 = x**2 + 1
        f4 = x**3 + 1

        # Größe der Grafik
        plt.figure(figsize=(10, 8))

        # Es werden vier Koordinatensysteme erzeugt und jeweils ein Funktionsgraph eingezeichnet
        
        # Subplot 1: semilogy
        plt.subplot(2, 2, 1)
        plt.semilogy(x, f1)
        plt.xlabel('x')
        plt.ylabel('f1(x)')
        plt.title('f1(x) = exp(x)')

        # Subplot 2: linear plot
        plt.subplot(2, 2, 2)
        plt.plot(x, f2)
        plt.xlabel('x')
        plt.ylabel('f2(x)')
        plt.title('f2(x) = x + 1')

        # Subplot 3: loglog
        plt.subplot(2, 2, 3)
        plt.loglog(x, f3)
        plt.xlabel('x')
        plt.ylabel('f3(x)')
        plt.title('f3(x) = x^2 + 1')

        # Subplot 4: loglog
        plt.subplot(2, 2, 4)
        plt.loglog(x, f4)
        plt.xlabel('x')
        plt.ylabel('f4(x)')
        plt.title('f4(x) = x^3 + 1')

        plt.tight_layout()
        plt.savefig('multiple_plots.png')

    # Wird für die Teilaufgabe etwas ungültiges eingesetzt, erscheint eine Fehlermeldung
    else:
        print("Diese Teilaufgabe gibt es nicht.")
        

#---------------------------------------------------
# Hauptprogramm

# Usereingaben
teilaufgabe = input("Welche Funktionen sollen gezeichnet werden? Teilaufgabe:")

# Zeichne die angeforderte Teilaufgabe 
funktion_plotten(teilaufgabe)
