import numpy as np
from numpy.random import default_rng


# Berechnung der Standardabweichung
def Statistik(Werte):
    
    # Mittelwert berechnen
    N = len(Werte)
    Mittelwert = sum(Werte) / N

    # Standardabweichung mit korrigierter empirischer Varianz (N-1 statt N)
    Stdabweichung1 = np.sqrt(sum((Werte - Mittelwert) ** 2) / (N-1))

    # (E((X-a)^2) - (E(X-a))^2) ** 0.5 mit Korrektur
    # a fehlte, wobei a = Mittelwert
    Stdabweichung2 = np.sqrt((N - 1) / N * (sum((Werte - Mittelwert) ** 2) / N - (sum((Werte - Mittelwert)/ N) ** 2)))

    #
    print("Mittelwert: ", Mittelwert, ", StdAbweichung 1: ", \
        Stdabweichung1, ", StdAbweichung 2: ", \
        Stdabweichung2, "Vergleich:", np.std(Werte, ddof=1))

###
rng = default_rng()
for i in range(7):
    Werte = rng.standard_normal(1000000)+10**i
    Statistik(Werte)