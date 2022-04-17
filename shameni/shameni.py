"""
    (c) 2020 Rodney Maniego Jr.
    Shameni
"""

import requests
from statistics import mean
from arkivist import Arkivist
from sometime import Sometime

class Gaze:
    def __init__(self, cachefile=None):
        autosave = True
        if cachefile is None:
            autosave = False
            cachefile = "cached.json"
        filename = "".join(cachefile.split(".")[:-1]) + "-prices.json"
        self.cached = Arkivist(cachefile, sort=True, autosave=autosave)
        self.prices = Arkivist(filename, sort=True, autosave=autosave)
        pass
    
    def ping(self):
        try:
            url = "http://presage.herokuapp.com/ping"
            return (requests.get(url).status_code == 200)
        except:
            return False
    
    def supported(self):
        try:
            url = f"http://presage.herokuapp.com/supported"
            return Arkivist().fetch(url).get("supported", [])
        except:
            return []
    
    def price(self, token):
        if isinstance(token, str):
            token = list(token.split(","))[0]
            date = Sometime().custom("%Y-%m-%d")
            price = self.prices.get(token, {}).get(date, -1)
            if price > 0:
                return price
            try:
                url = f"http://presage.herokuapp.com/tomorrow?tokens={token}"
                price = list(Arkivist().fetch(url).get(token, {}).values())[-1]
                if token not in self.prices:
                    self.prices.set(token, {})
                self.prices.find(token).set(date, price)
                return price
            except:
                pass
        return -1

    def request(self, tokens):
        if isinstance(tokens, str):
            status = requests.get(f"http://presage.herokuapp.com/request?tokens={tokens}")
            return (status.status_code == 200)
        return False
    
    def tomorrow(self, token):
        if isinstance(token, str):
            token = list(token.split(","))[0]
            date = Sometime().add(days=1).custom("%Y-%m-%d")
            predicted = self.cached.get(token, {}).get(date, -1)
            if predicted > 0:
                return predicted
            try:
                url = f"http://presage.herokuapp.com/tomorrow?tokens={token}"
                predicted = list(Arkivist().fetch(url).get(token, {}).values())[-1]
                if token not in self.cached:
                    self.cached.set(token, {})
                self.cached.find(token).set(date, predicted)
                return predicted
            except:
                pass
        return -1