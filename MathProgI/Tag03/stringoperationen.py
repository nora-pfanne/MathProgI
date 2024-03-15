'''
stringoperationen.py

Das Programmm stellt Methoden zu Verfügung, die eine Zeichenkette auf folgende Eigenschaften prüft:
- Ist die Zeichenkette ein Wortpalindrom?
- Ist die Zeichenkette ein Satzpalindrom?
- Sind zwei Zeichenketten Annagramme?
- Ist das Wort ein Isogramm?


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

def sonderzeichenEntfernen(wort: str):

    # Sonderzeichen, die aus dem Satz entfernt werden sollen
    sonderzeichen = [" ", ".", ";", ",", "?", "!", "-", "_"]

    # Entferne diese Sonderzeichen schrittweise
    for i in sonderzeichen:
        while i in wort:
            wort = wort.replace(i, "")
    
    wort = wort.lower()
    
    return wort


def istWortpalindrom(wort: str):

    # Abbruchbeding, wenn ein Palindrom vorliegt
    if len(wort) == 0 or len(wort) == 1:
        return True
    
    # Abbruchbedingung, wenn kein Palindrom vorliegt
    elif wort[0].lower() != wort[-1].lower():
        # sind die Character ungleich, liegt kein Palindrom vor
        return False
    
    # Rekursionsschritt
    else:
        return istWortpalindrom(wort[1:len(wort)-1])


def istSatzpalindrom(wort: str):

    # Entferne alle Sonderzeichen
    wort = sonderzeichenEntfernen(wort)

    # Führe "istWortpalindrom" auf die entstandene Zeichenkette aus
    return istWortpalindrom(wort)


def istAnagramm(wort: str, wort2: str):

    # Entferne alle Sonderzeichen aus den Zeichenketten
    wort = sonderzeichenEntfernen(wort)
    wort2 = sonderzeichenEntfernen(wort2)

    # Gehe schrittweise durch die erste Zeichenkette und überprüfe, ob dieser Buchstabe auch
    # in der zweiten Zeichenkette ist
    for buchstabe in wort:

        # Suche diesen Buchstaben in der zweiten Zeichenkette
        index = wort2.find(buchstabe)

        # Der Buchstabe konnte nicht gefunden werden => kein Anagramm
        if(index == -1):
            return False
        
        # Wurde der Buchstabe gefunden, wird er aus dem zweiten Wort gelöscht
        else:
            wort2 = wort2[:index] + wort2[index+1:]

    # Sind beide Zeichenketten leer, liegt ein Anagramm vor
    if(len(wort2) == 0):
        return True
    else:
        return False

def istIsogramm(wort: str):

    # Gehe die Zeichenkette durch und zähle nach, ob jeder Buchstabe genau einmal vorkommt
    for buchstabe in wort:

        # Abbruchbedingung: Ein Buchstabe kommt mehr als einmal vor
        if(wort.count(buchstabe) != 1):
            return False
    
    # Jeder Buchstabe ist nur einmal vorgekommen
    return True
    

#---------------------------------------------------
# Hauptprogramm

# Eingabe der Zeichenkette
wort = input("Gebe eine Zeichenkette ein:")
wort2 = input("Gebe eine Zeichenkette ein:")

# Überprüfung auf die Eigenschaften
print("Wortpalindrom:", istWortpalindrom(wort))
print("Satzpalindrom:", istSatzpalindrom(wort))
print("Annagramm:", istAnagramm(wort, wort2))
print("Isogramm:", istIsogramm(wort))
