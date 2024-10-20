from twilio.rest import Client
import requests

# CoinGecko API URL to get cryptocurrency prices
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'

# Alert parameters
ALERT_PRICE_BITCOIN = 30000  # Bitcoin price alert threshold
ALERT_PRICE_ETHEREUM = 2000   # Ethereum price alert threshold

# Twilio settings
TWILIO_SID = 'your_twilio_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
RECEIVER_PHONE_NUMBER = '+1234567890'

# Function to send SMS
def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Create and send the message
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=RECEIVER_PHONE_NUMBER
    )
    print(f'SMS sent: {message.sid}')

# Function to check prices and send SMS alert
def check_prices_with_sms():
    response = requests.get(API_URL)
    data = response.json()

    # Extract prices
    bitcoin_price = data['bitcoin']['usd']
    ethereum_price = data['ethereum']['usd']

    print(f"Bitcoin Price: ${bitcoin_price}")
    print(f"Ethereum Price: ${ethereum_price}")

    # Check if the prices meet alert conditions
    if bitcoin_price < ALERT_PRICE_BITCOIN:
        send_sms(f'Bitcoin price is below ${ALERT_PRICE_BITCOIN}. Current price: ${bitcoin_price}')

    if ethereum_price < ALERT_PRICE_ETHEREUM:
        send_sms(f'Ethereum price is below ${ALERT_PRICE_ETHEREUM}. Current price: ${ethereum_price}')

# Run the program
check_prices_with_sms()
