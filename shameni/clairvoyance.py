"""
    (c) 2020 Rodney Maniego Jr.
    Clairvoyance
"""

from arkivist import Arkivist
from sometime import Sometime

class Gaze:
    def __init__(self, cachefile=""):
        self.cached = Arkivist(cachefile, sort=True)
        pass
    
    def supported(self):
        try:
            url = f"http://presage.herokuapp.com/supported"
            return Arkivist().fetch(url).get("supported", [])
        except:
            pass
        return []
    
    def tomorrow(self, token, secret=""):
        if isinstance(token, str) and isinstance(secret, str):
            date = Sometime().add(days=1).custom("%Y-%m-%d")
            token = list(token.split(","))[0]
            predicted = self.cached.get(token, {}).get(date, -1)
            if predicted > 0:
                return predicted
            try:
                url = f"http://presage.herokuapp.com/tomorrow?coins={token}&secret={secret}"
                predicted = list(Arkivist().fetch(url).get(token, {}).values())[-1]
                dataset = self.cached.get(token, {})
                dataset.update({date: predicted})
                self.cached.update({token: dataset})
                return predicted
            except:
                pass
        return -1
    
    def today(self, token, secret=""):
        if isinstance(token, str) and isinstance(secret, str):
            date = Sometime().custom("%Y-%m-%d")
            token = list(token.split(","))[0]
            predicted = self.cached.get(token, {}).get(date, -1)
            if predicted > 0:
                return predicted
            try:
                url = f"http://presage.herokuapp.com/historical?coins={token}&secret={secret}"
                predicted = list(Arkivist().fetch(url).get(token, {}).values())[-2]
                dataset = self.cached.get(token, {})
                dataset.update({date: predicted})
                self.cached.update({token: dataset})
                return predicted
            except:
                pass
        return -1
    
    def historical(self, token, secret=""):
        if isinstance(token, str) and isinstance(secret, str):
            token = list(token.split(","))[0]
            cached = self.cached.get(token, {})
            day0 = cached.get(Sometime().add(days=1).custom("%Y-%m-%d"), -1)
            day6 = cached.get(Sometime().add(days=-5).custom("%Y-%m-%d"), -1)
            if min(day0, day6) > 0:
                predictions = {}
                for day in range(7):
                    day -= 1
                    date = Sometime().add(days=-day).custom("%Y-%m-%d")
                    price = cached.get(date, -1)
                    if price > 0:
                        predictions.update({date: price})
                return predictions
            try:
                url = f"http://presage.herokuapp.com/historical?coins={token}&secret={secret}"
                predictions = Arkivist().fetch(url).get(token, {})
                cached.update(predictions)
                self.cached.update({token: cached})
                return predictions
            except:
                pass
        return {}
    
    def historical(self, token, secret=""):
        if isinstance(token, str) and isinstance(secret, str):
            token = list(token.split(","))[0]
            cached = self.cached.get(token, {})
            day0 = cached.get(Sometime().add(days=1).custom("%Y-%m-%d"), -1)
            day6 = cached.get(Sometime().add(days=-5).custom("%Y-%m-%d"), -1)
            if min(day0, day6) > 0:
                predictions = {}
                for day in range(7):
                    day -= 1
                    date = Sometime().add(days=-day).custom("%Y-%m-%d")
                    price = cached.get(date, -1)
                    if price > 0:
                        predictions.update({date: price})
                return predictions
            try:
                url = f"http://presage.herokuapp.com/historical?coins={token}&secret={secret}"
                predictions = Arkivist().fetch(url).get(token, {})
                cached.update(predictions)
                self.cached.update({token: cached})
                return predictions
            except:
                pass
        return {}
        