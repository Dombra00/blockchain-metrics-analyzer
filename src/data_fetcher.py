import requests

class BlockchainDataFetcher:
    def __init__(self, api_url="https://blockchain.info/stats?format=json"):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

if __name__ == "__main__":
    fetcher = BlockchainDataFetcher()
    data = fetcher.fetch_data()
    
    if data:
        print(f"Bitcoin Market Price: ${data['market_price_usd']}")
        print(f"Total BTC in Circulation: {data['totalbc'] / 1e8} BTC")
        print(f"Estimated TX Volume: {data['estimated_transaction_volume_usd']} USD")
