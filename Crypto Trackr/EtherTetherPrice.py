import requests
import json

def get_crypto_prices():
    # URL of the CoinGecko API to get the prices
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd'

    # Sending request to the API and fetching the data
    response = requests.get(url)

    # Checking the status of the response
    if response.status_code == 200:
        # Converting the JSON data to a Python dictionary
        data = json.loads(response.text)

        # Extracting the prices
        bitcoin_price = data['bitcoin']['usd']
        ethereum_price = data['ethereum']['usd']
        tether_price = data['tether']['usd']

        # Displaying the prices
        print(f"Bitcoin Price: ${bitcoin_price}")
        print(f"Ethereum Price: ${ethereum_price}")
        print(f"Tether Price: ${tether_price}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

# Running the program
get_crypto_prices()
