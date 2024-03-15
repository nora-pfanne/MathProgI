'''
schaltjahr.py

Narges, Nora
Version 1.0, 14.03.2024
'''


def istSchaltjahr(jahr: int):

    #Ein Jahr ist ein Schaltjahr, wenn die Jahreszahl durch 4 teilbar ist, aber nicht durch 100, es sei denn, dass die
    # Jahreszahl auch durch 400 teilbar ist.

    if(((jahr % 4 == 0) and (jahr % 100 != 0)) or (jahr % 400 == 0)):
        return True
    else:
        return False


def jahreskalender(dateiname: str, jahr: int):

    width = 50

    monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    wochentage = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]

    # der Wochentag des 1. Januars nach Gauß
    w = (1 + 5 * (jahr-1) % 4  + 4* (jahr-1) % 100  + 6 * (jahr-1) % 400 ) % 7

    # Auf welchen Wochentag fällt der 1.?
    if(istSchaltjahr(jahr)):
        februar = 29
    else:
        februar = 28
    
    w_f = (w + 31) % 7
    w_mae = (w_f + februar) % 7
    w_a = (w_mae+ 31) % 7
    w_ma = (w_a+ 30) % 7
    w_jun = (w_ma + 31) % 7
    w_jul = (w_jun + 30) % 7
    w_au = (w_jul + 31) % 7
    w_s = (w_au + 31) % 7
    w_o = (w_s + 30) % 7
    w_n = (w_o + 31) % 7
    w_d = (w_n + 30) % 7

    erster_wochentag = [w, w_f, w_mae, w_a, w_ma, w_jun, w_jul, w_au, w_s, w_o, w_n, w_d]

    # Datei anlegen und öffnen
    datei = dateiname + ".txt"
    g = open(datei, "w")

    g.write(((width-4) // 2)* ' ' + str(jahr) + "\n")

    for i in range(len(monate)):

        g.write((width-len(monate[i]))* ' ' + monate[i] + "\n")
        g.write(width *'-' + '\n')

        tag_string = ""
    
        for j in range(1,7):
            tag_string += wochentage[j] + 15 * " "

            if(erster_wochentag[i] > j):
                tag_string += 3 * " "


        
        g.write(wochentage[0] + "\n")

    g.close()


jahreskalender('kalender', 2024)



print(istSchaltjahr(2000))
print(istSchaltjahr(2100))
print(istSchaltjahr(1404))
print(istSchaltjahr(2023))
print(istSchaltjahr(2024))