import requests

"""Api wrapper"""


class Api:
    isLoggedIn = False
    s = requests.Session()
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://opera4u.operaunitn.cloud",
    }

    def __init__(self):
        pass

    def login(self, username: str, password: str):
        data = {"coming_from": "", "username": username, "password": password}

        res = self.s.post(
            "https://opera4u.operaunitn.cloud/area-riservata/login",
            headers=self.headers,
            data=data,
        )
        res = self.s.get(
            "https://opera4u.operaunitn.cloud/profilo_utente", allow_redirects=False
        )

        isLoggedIn = res.status_code == 200

        if not isLoggedIn:
            if res.status_code == 302:
                print(res.status_code, res.reason, "Redirected")
            else:
                print(res.status_code, res.reason)

        return isLoggedIn
