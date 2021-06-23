from shameni import Gaze

crypto = Gaze("cached.json")
print("Cryptocurrencies:", ", ".join(crypto.supported()))

print("\n[Bitcoin]")
print("Prediction")
predicted = crypto.tomorrow("bitcoin")
print(f" - Tomorrow: {predicted:,.2f} USD")
predicted = crypto.today("bitcoin")
print(f" - Today: {predicted:,.2f} USD")

print("\nPrediction History")
for date, price in crypto.historical("bitcoin").items():
    print(f"{date}: {price} USD")



