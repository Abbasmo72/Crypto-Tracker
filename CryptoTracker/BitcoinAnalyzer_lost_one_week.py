import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# API settings to get Bitcoin prices
API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '7',  # For one week
}

# Fetch the data
response = requests.get(API_URL, params=params)
data = response.json()

# Extract prices and timestamps
prices = data['prices']
timestamps = [datetime.fromtimestamp(price[0] / 1000) for price in prices]  # Convert milliseconds to datetime
values = [price[1] for price in prices]

# Plotting the chart
plt.figure(figsize=(10, 5))
plt.plot(timestamps, values, marker='o', linestyle='-', color='blue')
plt.title('Bitcoin Price Over the Last Week')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
