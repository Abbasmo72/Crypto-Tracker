# Bitcoin-Ethereum-Tether-price
A simple program using Python language to price Bitcoin Ethereum Tether to USD

Analysis of the Cryptocurrency Price Fetching Program Using CoinGecko API
This Python program fetches and displays the prices of three popular cryptocurrencies—Bitcoin, Ethereum, and Tether—using the CoinGecko API. The program makes an API call to retrieve real-time data and prints the prices in USD. Here's a step-by-step breakdown of how the code works:

1. Importing Libraries:
The program uses two main libraries:
requests: This library is used to send HTTP requests to the API and retrieve data from the CoinGecko website.
json: This is used to parse the JSON data received from the API into a Python dictionary.
2. Defining the Function get_crypto_prices:
The function get_crypto_prices handles the process of making the API call, processing the response, and displaying the prices.
3. Making the API Request:
The API URL: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd
This URL fetches the current prices of Bitcoin, Ethereum, and Tether against USD.
The request is made using requests.get(url), which sends a GET request to the API endpoint.
4. Checking the API Response:
The program checks the response status code. If the status code is 200 (indicating success), it proceeds to process the data; otherwise, it prints an error message with the status code.
5. Processing and Extracting Data:
If the request is successful, the program uses json.loads(response.text) to convert the received JSON data into a Python dictionary.
From this dictionary, the program extracts the prices of Bitcoin, Ethereum, and Tether using the keys like 'bitcoin'['usd'].
6. Displaying the Prices:
After extracting the prices, the program prints the values for the following:
Bitcoin price in USD
Ethereum price in USD
Tether price in USD
7. Error Handling:
If the API response is not successful (any status code other than 200), an error message is displayed along with the corresponding status code.
Features and Use Cases:
This program is useful for users who want to track real-time cryptocurrency prices.
It can be easily extended to include additional cryptocurrencies or save the data in other formats, such as a file.
The program is also a solid foundation for larger projects that involve tracking and analyzing cryptocurrency data over time.
