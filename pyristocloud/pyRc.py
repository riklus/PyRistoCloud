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
