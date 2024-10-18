import requests

def get_bitcoin_price():
    # URL of CoinGecko API to get Bitcoin price in USD
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    # Sending a request to the API and getting the response
    response = requests.get(url)
    
    # Parsing the JSON response
    data = response.json()
    
    # Returning the Bitcoin price in USD
    return data['bitcoin']['usd']

# Displaying the Bitcoin price in USD
price = get_bitcoin_price()
print(f'Bitcoin price: ${price}')
