# shameni
The official Presage Python wrapper, a straightforward cryptocurrency prediction service.

Powered by [CoinGecko](https://www.coingecko.com/api/documentations/v3) and [Presage](http://presage.herokuapp.com/) API.

**DISCLAIMER:** All data generated by Presage and/or Clairvoyance does not indicate real cryptocurrency prices and does not constitute to an expert financial advice. Do your own research and only take financial advice from a certified financial expert. This website and the information contained herein is not intended to be a source of any financial advice with respect to the material presented, and the information and/or documents contained in this website do not constitute investment advice.

## Usage
**Import Package**
```python
from shameni import Gaze
```

**Initialization**
```python
# simple initialization
crypto = Gaze()

# cache data to file
crypto = Gaze("predictions.json")
```

**Prediction**
```python
# get supported cryptocurrency list
coins = crypto.supported()

for coin in coins:
    print(coin)

# predict next day prediction
prediction = crypto.tomorrow("bitcoin")

# get today's prediction
prediction = crypto.today("bitcoin")
```

**Historical Data**
Up to seven days of historical predictions
```python
history = crypto.historical("bitcoin")
for date, price in history.items():
    print(f"{date}: {price:,.2f} USD")
```