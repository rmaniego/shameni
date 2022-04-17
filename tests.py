from time import sleep

from shameni import Gaze
from maguro import Maguro

accuracies = Maguro("accuracy.json", delimiter=",")
crypto = Gaze("cached.json")

if crypto.ping():
    print("Presage is alive!")

    supported = crypto.supported()
    if not len(supported) or supported is None:
        supported = ["bitcoin"]
    crypto.request(",".join(supported))

    """print("[Prices]")
    for token in supported:
        for x in range(5):
            price = float(crypto.price(token))
            if price > 0:
                print(f" - {token.capitalize()}: {price:,.2f} USD")
                break
            sleep(1)"""

    print("[Predicted]")
    for token in supported:
        for x in range(5):
            price = float(crypto.tomorrow(token))
            if price > 0:
                print(f" - {token.capitalize()}: {price:,.2f} USD")
                break
            sleep(1)



