"""
    (c) 2020 Rodney Maniego Jr.
    Shameni
"""

import requests
from statistics import mean

from arkivist import Arkivist
from sometime import Sometime

class Gaze:
    def __init__(self, cachefile=""):
        self.cached = Arkivist(cachefile, sort=True)
        pass
    
    def ping(self):
        try:
            status = requests.get("http://presage.herokuapp.com/ping")
            return (status.status_code == 200)
        except:
            pass
        return False
    
    def supported(self):
        try:
            url = f"http://presage.herokuapp.com/supported"
            return Arkivist().fetch(url).get("supported", [])
        except:
            pass
        return []
    
    def price(self, token):
        try:
            currency = "usd"
            date = Sometime().custom("%Y-%m-%d")
            prices = self.prices.get(date, {})
            actual = prices.get(token, -1)
            if actual > 0:
                return actual
            url = f"http://presage.herokuapp.com/price?coins={token}&vs_currencies={currency}"
            prices.update(Arkivist().fetch(url).show())
            price = prices.get(token, {}).get(currency, -1)
            for token, data in prices:
                token_data = self.cached.get(token, {})
                token_price = token_data.get("prices", {})
                price = data.get(currency, -1)
                if price > 0:
                    token_price.update({date: price})
                    token_data.update({"prices": token_price})
                    self.cached.set(token, token_data)
            return price
        except:
            pass
        return -1

    def wavg(self, token, days):
        token = list(token.split(","))[0]
        url = f"http://presage.herokuapp.com/wavg?coins={token}"
        return Arkivist().fetch(url).show().get(token, {}).get(days, -1)

    def request(self, coins):
        if isinstance(coins, str):
            status = requests.get(f"http://presage.herokuapp.com/request?coins={coins}")
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
                url = f"http://presage.herokuapp.com/tomorrow?coins={token}"
                predicted = list(Arkivist().fetch(url).get(token, {}).values())[-1]
                token_predictions.update({date: predicted})
                token_data.update("predictions", token_predictions)
                self.cached.update({token: token_data})
                return predicted
            except:
                pass
        return -1

    def distance(self, token):
        token = list(token.split(","))[0]
        url = f"http://presage.herokuapp.com/distance?coins={token}"
        return Arkivist().fetch(url).show().get("distance", -1)