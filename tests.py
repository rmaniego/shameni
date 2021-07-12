from time import sleep

from shameni import Gaze
from maguro import Maguro

accuracies = Maguro("accuracy.json", delimiter=",")
crypto = Gaze("cached.json")

if crypto.ping():
    supported = crypto.supported()
    print("Cryptocurrencies:", ", ".join(supported))

    supported = ["bitcoin"]
    for token in supported:
        wavg = crypto.wavg(token, 1)
        if wavg > 0:
            print(f"1-day WAVG: {wavg}")
        
        crypto.request(token)
        print(f"\n[{token.capitalize()}]")
        for x in range(5):
            tomorrow = crypto.tomorrow(token)
            if tomorrow > 0:
                print("Prediction")
                print(f" - Tomorrow: {tomorrow:,.2f} USD")
                break
            sleep(1)
        for x in range(5):
            gap = crypto.distance(token)
            if gap > 0:
                print(f" - Distance: {gap:,.6f}")
                break



