from shameni import Gaze
from maguro import Maguro

accuracies = Maguro("accuracy.json", delimiter=",")
crypto = Gaze("cached.json")
print("Cryptocurrencies:", ", ".join(crypto.supported()))

for x in range(5):
    if crypto.ping():
        print("\n[Bitcoin]")
        print("Prediction")
        predicted = crypto.tomorrow("bitcoin")
        print(f" - Tomorrow: {predicted:,.2f} USD")
        predicted = crypto.today("bitcoin")
        if predicted > 0:
            actual = crypto.price("bitcoin")
            accuracy = round((100 - (((predicted - actual) / actual) * 100)), 2)
            print(f" - Today: {predicted:,.2f} ({actual:,.2f}) USD")
            avg_accuracy = crypto.accuracy("bitcoin")
            print(f" - Accuracy: {accuracy:,.2f}% ({avg_accuracy:,.2f}%)")
            accuracies.append(accuracy)
        print("\nPrediction History")
        for date, price in crypto.historical("bitcoin").items():
            print(f"{date}: {price:,.2f} USD")
    break



