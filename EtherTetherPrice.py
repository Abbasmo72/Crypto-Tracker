import requests

import json

def get_crypto_prices():
    # URL API صرافی CoinGecko برای دریافت قیمت‌ها
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd'

    # درخواست به API و دریافت داده‌ها
    response = requests.get(url)

    # بررسی وضعیت پاسخ
    if response.status_code == 200:
        # تبدیل داده‌های JSON به دیکشنری پایتون
        data = json.loads(response.text)

        # استخراج قیمت‌ها
        bitcoin_price = data['bitcoin']['usd']
        ethereum_price = data['ethereum']['usd']
        tether_price = data['tether']['usd']

        # نمایش قیمت‌ها
        print(f"Bitcoin Price: ${bitcoin_price}")
        print(f"Ethereum Price: ${ethereum_price}")
        print(f"Tether Price: ${tether_price}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

# اجرای برنامه
get_crypto_prices()
