"""
    (c) 2020 Rodney Maniego Jr.
    Shameni
"""

import requests
from statistics import mean

from arkivist import Arkivist
from sometime import Sometime

class Gaze:
    def __init__(self, cachefile="", prices=""):
        self.cached = Arkivist(cachefile, sort=True)
        self.prices = Arkivist(prices, sort=True)
        pass
    
    def ping(self):
        status = requests.get("http://presage.herokuapp.com/ping")
        if status.status_code == 200:
            return True
        return False

    def accuracy(self, coin, currency="usd"):
        accuracies = []
        predictions = self.cached.get(coin, {})
        for date, predicted in predictions.items():
            actual = self.prices.get(date, {}).get(coin, {}).get(currency, -1)
            if actual > 1:
                prediction_accuracy = (100 - (((predicted - actual) / actual) * 100))
                if prediction_accuracy > 100:
                    prediction_accuracy = (100 - (prediction_accuracy - 100))
                accuracies.append(prediction_accuracy)
        if len(accuracies) > 0:
            return mean(accuracies)
        return 0
    
    def price(self, coin, currency="usd", date=None):
        try:
            if not isinstance(date, str):
                date = Sometime().custom("%Y-%m-%d")
            prices = self.prices.get(date, {})
            actual = prices.get(coin, -1)
            if actual > 0:
                return actual
            url = f"http://presage.herokuapp.com/price?coins={coin}&vs_currencies={currency}"
            prices.update(Arkivist().fetch(url).show())
            self.prices.set(date, prices)
            return prices.get(coin, {}).get(currency, -1)
        except:
            pass
        return -1
    
    def supported(self):
        try:
            url = f"http://presage.herokuapp.com/supported"
            return Arkivist().fetch(url).get("supported", [])
        except:
            pass
        return []
    
    def tomorrow(self, token, currency="usd", secret=""):
        if isinstance(token, str) and isinstance(currency, str) and isinstance(secret, str):
            date = Sometime().add(days=1).custom("%Y-%m-%d")
            token = list(token.split(","))[0]
            predicted = self.cached.get(token, {}).get(date, -1)
            if predicted > 0:
                return predicted
            try:
                url = f"http://presage.herokuapp.com/tomorrow?coins={token}&currency={currency}&secret={secret}"
                predicted = list(Arkivist().fetch(url).get(token, {}).values())[-1]
                dataset = self.cached.get(token, {})
                dataset.update({date: predicted})
                self.cached.update({token: dataset})
                return predicted
            except:
                pass
        return -1
    
    def today(self, token, currency="usd", secret=""):
        if isinstance(token, str) and isinstance(currency, str) and isinstance(secret, str):
            date = Sometime().custom("%Y-%m-%d")
            token = list(token.split(","))[0]
            predicted = self.cached.get(token, {}).get(date, -1)
            if predicted > 0:
                return predicted
            try:
                url = f"http://presage.herokuapp.com/historical?coins={token}&currency={currency}&secret={secret}"
                predicted = list(Arkivist().fetch(url).get(token, {}).values())[-2]
                dataset = self.cached.get(token, {})
                dataset.update({date: predicted})
                self.cached.update({token: dataset})
                return predicted
            except:
                pass
        return -1
    
    def historical(self, token, currency="usd", secret=""):
        if isinstance(token, str) and isinstance(currency, str) and isinstance(secret, str):
            token = list(token.split(","))[0]
            cached = self.cached.get(token, {})
            day0 = cached.get(Sometime().add(days=1).custom("%Y-%m-%d"), -1)
            day6 = cached.get(Sometime().add(days=-5).custom("%Y-%m-%d"), -1)
            if min(day0, day6) > 0:
                predictions = {}
                for day in range(7):
                    day -= 1
                    date = Sometime().add(days=-day).custom("%Y-%m-%d")
                    token_prediction = cached.get(date, -1)
                    if token_prediction > 0:
                        predictions.update({date: token_prediction})
                return predictions
            try:
                url = f"http://presage.herokuapp.com/historical?coins={token}&currency={currency}&secret={secret}"
                predictions = Arkivist().fetch(url).get(token, {})
                cached.update(predictions)
                self.cached.update({token: cached})
                return predictions
            except:
                pass
        return {}
        