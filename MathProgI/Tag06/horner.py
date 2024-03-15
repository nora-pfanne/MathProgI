'''
horner.py

In diesem Programm werden Ansätze zur Berechnung der Exponentialfunktion in Hinblick
auf ihre Effizienz verglichen.
    

Narges, Nora
Version 1.0, 11.03.2024
'''

# Bibliotheke
import matplotlib.pyplot as plt
import math
import numpy as np

'''
Berechnung der Exponentialfunktion mit dem Hornerschema an der Stelle x, 
abgeschätzt bis zum n-ten Reihenglied.

Eingabe:
    x: float
    n: int
    a: List<float>

Ausgabe:
    y: float
'''
def hornerschema(x, n: int, a):
    
    b = a[-1]  

    while(n != 1):

        n -= 1
        b = a[n-1] + x * b
        
    return b 


def taylor_arctan(x, n: int):

    # Koeffizienten für das Hornerschema
    a = []

    for k in range(n):

        # Bestimme die Koeffizienten
        a_k = 1

        if(k % 2):
            a_k = (-1) * 1 /(2 * k + 1)
        else:
            a_k = 1 * 1 /(2 * k + 1)

        a += [0, a_k]
    
    return a


def taylor_sinus(x, n: int):

    # Koeffizienten für das Hornerschema
    a = []

    for k in range(n):

        # Bestimme die Koeffizienten
        a_k = 1

        if(k % 2):
            a_k = (-1) * 1 / math.factorial(2 * k + 1)
        else:
            a_k = 1 * 1 / math.factorial(2 * k + 1)

        a += [0, a_k]
    
    return a


def taylor_log(x, n: int):

    # Koeffizienten für das Hornerschema
    a = [0]

    for k in range(1,n):

        # Bestimme die Koeffizienten
        a_k = 1

        if(k % 2):
            a_k =  1 / k
        else:
            a_k =  - 1 / k

        a += [a_k]
    
    return a

'''
Eingabe:
    x: float
    n: int

Ausgabe:
    y: float
'''
def e_n(x, n: int):
    
    b = a(n)
    
    while(n != 0):

        b = a(n-1) + x * b
        n -= 1

    return b 

    
def a(n):
    return 1.0 / math.factorial(n)


'''
Funktion aus der Aufgabenstellung

Eingabe:
    x: float
    n: int

Ausgabe:
    y: float
'''
def exponentialfunktion(x, n):

    if x < 0.0:
        return 1.0 / exponentialfunktion(-x, n)

    elif x >= 1.0:
        tmp = exponentialfunktion(x/2.0, n)
        return tmp * tmp

    else:
        # Berechnung von e_n(x)
        y = e_n(x,n)
        return y

    


#---------------------------------------------------
# Hauptprogramm

'''
# Arctan

# x-Werte
testintervall = np.arange(-1.0,1.0,0.01).tolist()

# y-Werte
for n in range(2, 11, 2):

    y = []

    for x in testintervall:

        a = taylor_arctan(x, n)
        y += [hornerschema(x,n,a)]

    # Subplot:
    plt.subplot(2, 3, n//2)
    plt.plot(testintervall, y)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Titel setzen
    plt.title(n)

plt.tight_layout()


# Vergleich von hornerschema(x) und math.sin(x)

# y-Werte
y = []
y_2 = []

# Generiere die Funktionswerte
for x in testintervall:
        y += [math.atan(x)]
        a = taylor_arctan(x, 10)
        y_2 += [hornerschema(x,10,a)]

plt.subplot(2, 3, 6)
plt.plot(testintervall, y)
plt.plot(testintervall, y_2)
plt.title('Vergleich')
plt.savefig('hornerschema_arctan.png')
plt.cla()
plt.clf()


# Relativer Fehler
fehler = []

# Relativen Fehler berechnen
for x in testintervall:
     a = taylor_arctan(x, 10)
     fehler += [abs(math.atan(x) - hornerschema(x,10,a)) / math.atan(x)]

plt.loglog(testintervall, fehler)
plt.title('Relativer Fehler')

plt.savefig('fehler_horner_arctan.png')
plt.cla()
plt.clf()


# Sinus

# x-Werte
testintervall_sinus = np.arange(-math.pi/2, math.pi/2, 0.01).tolist()

# y-Werte
for n in range(2, 11, 2):

    y = []

    for x in testintervall_sinus:

        a = taylor_sinus(x, n)
        y += [hornerschema(x,n,a)]

    # Subplot:
    plt.subplot(2, 3, n//2)
    plt.plot(testintervall_sinus, y)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Titel setzen
    plt.title(n)

plt.tight_layout()


# Vergleich von hornerschema(x) und math.sin(x)

# Skalierung der Achsen (nur für n = 2)
y = []
y_2 = []

# Generiere die Funktionswerte
for x in testintervall_sinus:
        y += [math.sin(x)]
        a = taylor_sinus(x, 10)
        y_2 += [hornerschema(x,10,a)]

plt.subplot(2, 3, 6)
plt.plot(testintervall_sinus, y)
plt.plot(testintervall_sinus, y_2)
plt.title('Vergleich')
plt.savefig('hornerschema_sinus.png')
plt.cla()
plt.clf()

# Relativer Fehler
fehler = []

# Relativen Fehler berechnen
for x in testintervall_sinus:
     a = taylor_sinus(x, 10)
     fehler += [abs(math.sin(x) - hornerschema(x,10,a)) / math.sin(x)]

plt.semilogy(testintervall_sinus, fehler)
plt.title('Relativer Fehler')

plt.savefig('fehler_horner_sinus.png')
plt.cla()
plt.clf()


# Logarithmus

# x-Werte
testintervall_log = np.arange(0.5, 2.0, 0.01).tolist()

# y-Werte
for n in range(2, 11, 2):

    y = []

    for x in testintervall_log:

        a = taylor_log(x, n)
        y += [hornerschema(x-1,n,a)]

    # Subplot:
    plt.subplot(2, 3, n//2)
    plt.plot(testintervall_log, y)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Titel setzen
    plt.title(n)

plt.tight_layout()


# Vergleich von hornerschema(x) und math.sin(x)

# Skalierung der Achsen (nur für n = 2)
y = []
y_2 = []

# Generiere die Funktionswerte
for x in testintervall_log:
        y += [math.log(x)]
        a = taylor_log(x, 10)
        y_2 += [hornerschema(x-1,10,a)]

plt.subplot(2, 3, 6)
plt.plot(testintervall_log, y)
plt.plot(testintervall_log, y_2)
plt.title('Vergleich')
plt.savefig('hornerschema_log.png')
plt.cla()
plt.clf()

# Relativer Fehler
fehler = []

# Relativen Fehler berechnen
for x in testintervall_log:
     a = taylor_log(x, 10)
     fehler += [abs(math.log(x) - hornerschema(x-1,10,a)) / math.log(x)]

plt.loglog(testintervall_log, fehler)
plt.title('Relativer Fehler')

plt.savefig('fehler_horner_log.png')
plt.cla()
plt.clf()


# Approximation reeller Zahlen

testintervall = np.arange(1,100,1).tolist()

y = []

# Generiere die Funktionswerte
for n in testintervall:
        a = taylor_arctan(1, n)
        y += [abs(math.pi - 4 * hornerschema(1,n,a)) / math.pi]

plt.plot(testintervall, y)
plt.title('pi approximieren')
plt.savefig('pi.png')
plt.cla()
plt.clf()



y = []

# Generiere die Funktionswerte
for n in testintervall:
        a = taylor_log(2, n)
        y += [abs(np.log(2) - hornerschema(1, n, a)) / np.log(2)]

plt.loglog(testintervall, y)
plt.title('ln(2) approximieren')
plt.savefig('ln.png')
plt.cla()
plt.clf()
'''
