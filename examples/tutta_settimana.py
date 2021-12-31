from pyristocloud import pyRc

# Prenota il posto all'orario indicato se disponibile

rc = pyRc.Api()
logged = rc.login("nome.cognome@studenti.unitn.it", "pass")

if logged:
    print("Login effettuato!")
else:
    print("Errore login.")
    exit()

giorno_inizio_settimana = 3
mese = "12"
anno = "2022"
mensa = "mensa_povo0"
orario_inizio = "13:15"

# Itero una settimana
for giorno in range(giorno_inizio_settimana, giorno_inizio_settimana + 7):
    data = "/".join([str(giorno), mese, anno])
    for orario in rc.get_orari_prenotati(mensa, data):
        # Prenoto solo se è l'orario giusto
        if orario["orario_inizio"] != orario_inizio:
            continue

        if orario["isBookale"]:
            if rc.salva_prenotazione(mensa, data, orario["id"]):
                print(
                    "Ho prenotato un posto per le:",
                    orario["orario_inizio"],
                    data,
                    mensa,
                )
                break
            else:
                print(
                    "Errore nella prenotazione di:",
                    orario["orario_inizio"],
                    data,
                    mensa,
                )
        else:
            print("Non è possibile prenotare:", orario["orario_inizio"], data, mensa)
