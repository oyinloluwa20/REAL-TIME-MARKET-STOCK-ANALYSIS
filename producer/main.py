from extract import connect_to_api, extract_data


def main():
    api_response = connect_to_api()
    extracted_data = extract_data(api_response)
    for stock in extracted_data:
        result = {
            "timestamp": stock.get("timestamp"),
            "symbol": stock.get("symbol"),
            "open": stock.get("open"),
            "high": stock.get("high"),
            "low": stock.get("low"),
            "close": stock.get("close"),
            "volume": stock.get("volume")
        }
        print(result)

    