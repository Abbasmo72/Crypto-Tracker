import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

# نمایش قیمت بیت‌کوین به دلار
price = get_bitcoin_price()
print(f'Bitcoin price ${price}')
