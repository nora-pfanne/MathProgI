import numpy as np

def Sarrus(A):
    determinante = 0.0
    n = len(A)
    index = np.concatenate((np.arange(n), np.arange(n-1)))
    for i in range(n):
        produkt = 1.0
        for j in range(n):
            '''
            alte Fehlermeldung: 
            produkt *= A[j, index[i+j]]
            IndexError: index 3 is out of bounds for axis 1 with size 3
            '''
            # Sicherstellen, dass der Index im gültigen Bereich liegt
            index_val = index[i+j] % n  
            produkt *= A[j, index_val]
        determinante += produkt
    index = np.concatenate((np.arange(n,0,-1), np.arange(n,1,-1)))
    for i in range(n):
        produkt = 1.0
        for j in range(n):
            # Sicherstellen, dass der Index im gültigen Bereich liegt
            index_val = index[i+j] % n  
            produkt *= A[j, index_val]
        determinante -= produkt
    return determinante


# Testen der Funktion mit einer Beispielmatrix
A = np.array([[1, 2, -9],
              [4, 7, 6],
              [7, 8, 9]])

# Aufrufen der Sarrus-Funktion und Ausgabe der Determinante
print("Determinante nach der Sarrus-Regel:", Sarrus(A))

# Vergleichen mit dem Wert, den die NumPy-Funktion linalg.det() liefert
print("Determinante mit NumPy:", np.linalg.det(A))
