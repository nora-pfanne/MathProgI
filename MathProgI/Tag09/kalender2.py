def ist_schaltjahr(jahr):
    """Funktion zur Überprüfung, ob ein Jahr ein Schaltjahr ist"""
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def kalender_monat(monat, jahr):
    """Funktion zur Erstellung des Kalenders für einen bestimmten Monat"""
    monatsnamen = ["Januar", "Februar", "März", "April", "Mai", "Juni",
                   "Juli", "August", "September", "Oktober", "November", "Dezember"]
    tage_im_monat = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

    if ist_schaltjahr(jahr):
        tage_im_monat[1] = 29

    kalender = f"{jahr}\n{monatsnamen[monat-1].upper()}\n{'-'*35}\n"

    start_tag = sum(tage_im_monat[:monat-1]) % 7  # Starttag des Monats (0: Montag, 1: Dienstag, ..., 6: Sonntag)

    for tag in range(1, tage_im_monat[monat-1] + 1):
        wochentag = wochentage[(start_tag + tag - 1) % 7]
        if wochentag == "Montag":
            kalender += f"\n{wochentag:9s}"
        else:
            kalender += f"{wochentag:10s}"
        kalender += f"{tag:2d} "
        if (tag + start_tag) % 7 == 0:
            kalender += "\n"

    kalender += "\n\n"
    return kalender

def Jahreskalender(dateiname, jahr):
    """Funktion zur Erstellung des Jahreskalenders und Speicherung in einer Textdatei"""
    with open(dateiname, 'w') as file:
        for monat in range(1, 13):
            file.write(kalender_monat(monat, jahr))

# Beispielaufruf
Jahreskalender("jahreskalender_2024.txt", 2024)
print("Jahreskalender wurde erstellt und in jahreskalender_2024.txt gespeichert.")
