import requests

"""Api wrapper"""


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

        Examples:
            .. code:: python

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

        if not self.isLoggedIn:
            print("[!] Login Failed:", res.status_code, res.reason)

        return self.isLoggedIn

    def get_orari_prenotati(self, mensa: str, data: str):
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
            dict: dizionario contentente gli orari.

        Examples:
            .. code:: python

                >>> api.get_orari_prenotati("mensa_tgar", "31/12/2021")
                True
        """
        if not self.isLoggedIn:
            print("[!] Not logged in!")
            return None

        if not (mensa in self.refettori):
            print("[!] Mensa non trovata.")
            return None

        data = {"refettori_id": self.refettori[mensa], "data": data}

        res = self.s.post(
            "https://opera4u.operaunitn.cloud/prenota_tavolo/get_orari_prenotati",
            headers=self.headers,
            data=data,
        )
        if not res.ok:
            print(res.status_code, res.reason)
            return None

        return res.json()

    def salva_prenotazione(self, mensa: str, data: str, id: str) -> bool:
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
            bool: prenotazione effettuata.

        Examples::
                >>> api.salva_prenotazione("mensa_tgar", "31/12/2021", "49")
                True
        """
        if not self.isLoggedIn:
            print("[!] Not logged in!")
            return False

        if not (mensa in self.refettori or mensa in self.saleId):
            print("[!] Mensa non trovata.")
            return False

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
        return res.ok
