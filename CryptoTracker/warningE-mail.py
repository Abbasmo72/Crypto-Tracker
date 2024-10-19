import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CoinGecko API URL to get cryptocurrency prices
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'

# Alert parameters
ALERT_PRICE_BITCOIN = 30000  # Bitcoin price alert threshold
ALERT_PRICE_ETHEREUM = 2000   # Ethereum price alert threshold

# Email settings
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_email_password'
RECEIVER_EMAIL = 'receiver_email@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Function to send email
def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up the server connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check prices and send alert
def check_prices():
    response = requests.get(API_URL)
    data = response.json()

    # Extract prices
    bitcoin_price = data['bitcoin']['usd']
    ethereum_price = data['ethereum']['usd']

    print(f"Bitcoin Price: ${bitcoin_price}")
    print(f"Ethereum Price: ${ethereum_price}")

    # Check if the prices meet alert conditions
    if bitcoin_price < ALERT_PRICE_BITCOIN:
        send_email('Bitcoin Price Alert', f'Bitcoin price is below ${ALERT_PRICE_BITCOIN}. Current price: ${bitcoin_price}')

    if ethereum_price < ALERT_PRICE_ETHEREUM:
        send_email('Ethereum Price Alert', f'Ethereum price is below ${ALERT_PRICE_ETHEREUM}. Current price: ${ethereum_price}')

# Run the program
check_prices()
