import sys
import requests

while True:
    try:
        bitcoin_amount = sys.argv[1]
        if type(bitcoin_amount) == str:
            bitcoin_amount = float(bitcoin_amount)
            break
        elif type(bitcoin_amount) == int:
            sys.exit("We do not accept text as a value")
        else:
            sys.exit("Wrong value provided")
    except requests.RequestException:
        pass


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()
price = response["bpi"]["USD"]["rate"].replace(",", "")
price = float(price)
amount = bitcoin_amount * price
print(f"${amount:,.4f}")