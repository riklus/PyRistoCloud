from typing import TypedDict

from html.parser import HTMLParser

import requests

"""Semplice Api wrapper per prenotare la mensa RistoCloud UNITN"""


class orario(TypedDict):
    id: int
    tipo_pasto_id: int
    orario_inizio: str
    orario_fine: str
    totale_prenotato: int
    totale_prenotabile: int
    percentuale: int
    isBookale: bool
    isEditable: bool


class PrenotazioneNoParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "button":
            for attr in attrs:
                if attr[0] == "data-prenotazione":
                    self.data = attr[1]


class Api:
    isLoggedIn = False
    s = requests.Session()
    refettori = {
        "bar_mesiano": 9,
        "mensa_tgar": 1,
        "mensa_mesiano": 3,
        "mensa_povo0": 4,
        "mensa_povo1": 5,
    }

    saleId = {
        "bar_mesiano": 6,
        "mensa_tgar": 3,
        "mensa_mesiano": 4,
        "mensa_povo0": 1,
        "mensa_povo1": 2,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20200731 Firefox/37.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
    }

    def __init__(self):
        pass

    def login(self, username: str, password: str) -> bool:
        """Funzione di login.

        Args:
            username (str): email@studenti.unitn.it.
            password (str): La password di RistoCloud.

        Returns:
            bool: successo del login.

        Examples::
            >>> api.login("mario.rossi@studenti.unitn.it", "password1234")
            True
        """
        data = {"coming_from": "", "username": username, "password": password}

        res = self.s.post(
            "https://opera4u.operaunitn.cloud/area-riservata/login",
            headers=self.headers,
            data=data,
            allow_redirects=False,
        )

        # Il login restituisce 302 se ha funzionato e 200 se fallisce.
        self.isLoggedIn = res.status_code == 302

        return self.isLoggedIn

    def get_orari_prenotati(self, mensa: str, data: str) -> list[orario]:
        """Ritorna gli orari disponibili nella mensa e data indicata.
        Refettori disponibili:
            bar_mesiano
            mensa_tgar
            mensa_mesiano
            mensa_povo0
            mensa_povo1

        Args:
            mensa (str): La mensa di cui vuoi sapere gli orari.
            data (str): La data di cui vuoi sapere gli orari.

        Returns:
            list[orario]: lista contentente gli orari.
            None: Errore nella richiesta.

        Examples::
            >>> api.get_orari_prenotati("mensa_tgar", "31/12/2021")
            [
                {
                    "id": 22,
                    "tipo_pasto_id": 3,
                    "orario_inizio": "12:15",
                    "orario_fine": "12:30",
                    "totale_prenotato": 0,
                    "totale_prenotabile": 46,
                    "percentuale": 0,
                    "isBookale": True,
                    "isEditable": True
                }
            ]
        """
        if not self.isLoggedIn:
            raise Exception("Not logged in!")

        if not (mensa in self.refettori):
            raise ValueError("La mensa richiesta non esiste o non è disponibile.")

        data = {"refettori_id": self.refettori[mensa], "data": data}

        res = self.s.post(
            "https://opera4u.operaunitn.cloud/prenota_tavolo/get_orari_prenotati",
            headers=self.headers,
            data=data,
        )
        if res.ok:
            return res.json()["reservations"]
        else:
            return None

    def salva_prenotazione(self, mensa: str, data: str, id: str) -> str:
        """Prenota il posto in mensa in una certa data.
        Refettori disponibili:
            bar_mesiano
            mensa_tgar
            mensa_mesiano
            mensa_povo0
            mensa_povo1

        Args:
            mensa (str): La mensa dove vuoi prenotare il posto.
            data (str): La data nella quale vuoi prenotare il posto.
            id (str): L'id dell'orario nel quale vuoi prenotare il posto.

        Returns:
            str: ID della prenotazione effettuata.
            None: Prenotazione non registrata nel Database (Potrebbe comunque arrivare l'email di conferma)

        Examples::
            >>> api.salva_prenotazione("mensa_tgar", "31/12/2021", "49")
            172822
        """
        if not self.isLoggedIn:
            raise Exception("Not logged in!")

        if not (mensa in self.refettori or mensa in self.saleId):
            raise ValueError("La mensa richiesta non esiste o non è disponibile.")

        data = {
            "data": data,
            "orarioId": id,
            "refettorioId": self.refettori[mensa],
            "saleId": self.saleId[mensa],
            "prenotati": "1",
            "prenotazioneOldId": "",
        }

        res = self.s.post(
            "https://opera4u.operaunitn.cloud/prenota_tavolo/salva_prenotazione",
            headers=self.headers,
            data=data,
        )

        if not res.ok:
            return None

        prenotazioneNoParser = PrenotazioneNoParser()
        prenotazioneNoParser.feed(res.text)

        if hasattr(prenotazioneNoParser, "data"):
            return prenotazioneNoParser.data
        else:
            return None

    def annulla_prenotazione(self, id: str) -> bool:
        """Annulla una prenotazione tramite il suo id.

        Args:
            id (str): Id della prenotazione.

        Returns:
            bool: Successo della cancellazione.

        Examples::
            >>> api.annulla_prenotazione("172822")
            True
        """
        if not self.isLoggedIn:
            raise Exception("Not logged in!")

        data = {"id": id}

        res = self.s.post(
            "https://opera4u.operaunitn.cloud/prenota_tavolo/annulla_prenotazione",
            headers=self.headers,
            data=data,
        )

        return res.ok
