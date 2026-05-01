import requests
from config import headers, url, logger



def connect_to_api():
    stocks = ['', 'AAPL', 'GOOGL', 'AMZN', 'TSLA', 'META']
    json_response = []
    for stock in stocks:
        try:
            querystring = {"function":"TIME_SERIES_INTRADAILY","symbol":stock,"outputsize":"compact","interval":"5min","datatype":"json"}
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()  # Check if the request was successful
            logger.info(f"Successfully connected to the API for stock: {stock}.")
            json_response.append(response.json())
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to the API for stock {stock}: {e}")
            break
    return json_response
    
def extract_data(response):
    extracted_data = []
    for stock_data in response:
        try:
            symbol = stock_data.get("Meta Data", {}).get("2. Symbol", "N/A")
            time_series = stock_data.get("Time Series (5min)", {})
            for timestamp, data in time_series.items():
                extracted_data.append({
                    "timestamp": timestamp,
                    "symbol": symbol,
                    "open": data.get("1. open"),
                    "high": data.get("2. high"),
                    "low": data.get("3. low"),
                    "close": data.get("4. close"),
                    "volume": data.get("5. volume")
                })
            logger.info(f"Successfully extracted data for stock.")
        except KeyError as e:
            logger.error(f"Error extracting data: {e}")
    return extracted_data

# url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"TIME_SERIES_DAILY","symbol":"MSFT","outputsize":"compact","datatype":"json"}

# headers = {
# 	"x-rapidapi-key": "72e347c282msh9e086f3c91588e5p109faejsn097d01258f99",
# 	# "x-rapidapi-key": "209f1fb9bfmsh027cc5ffc4ff43ap121569jsn52052baf7ca0",
# 	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

response = requests.get(url, headers=headers, params=querystring)

print(response.json())