from datetime import date

from pyristocloud import pyRc

rc = pyRc.Api()
logged = rc.login("nome.cognome@studenti.unitn.it", "pass")

if logged:
    print("Login effettuato!")
else:
    print("Errore login.")
    exit()

mensa = "mensa_tgar"
data = date.today().strftime("%d/%m/%y")
orario_inizio = "13:15"

orari_prenotati = rc.get_orari_prenotati(mensa, data)
# Controllo se l'orario che voglio prenotare è disponibile
for orario in orari_prenotati:
    if orario["isBookale"] and orario["orario_inizio"] == orario_inizio:
        if rc.salva_prenotazione(mensa, data, orario["id"]):
            print("Prenotazione effettuata:", mensa, data, orario_inizio)
        else:
            print("Errore nella prenotazione:", mensa, data, orario_inizio)
        # Esco se l'orario non è disponibilie
        exit()

print("Orario", orario_inizio, "non trovato per il", data, "in", mensa)
