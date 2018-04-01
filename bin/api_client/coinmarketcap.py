from api_client.base import BaseAPIClient
import json

class CoinMarketCapAPIClient(BaseAPIClient):
    
    def __init__(self):
        self.API_URL = 'https://api.coinmarketcap.com/v1'
        self.COINS_PATH = 'ticker'
    
    def get_prices(self):
        """
        Get a list of coins and its prices in USD
        :return:
            ticker	[string]
            rank	[int]
            price_usd	[float]
        """
        response = self._call(self.API_URL + '/' + self.COINS_PATH)
        response_json = json.loads(response.content.decode('utf-8'))
        prices = []        
        for coin in response_json:
            item = {}
            item['ticker'] = coin['symbol']
            item['rank'] = int(coin['rank'])
            item['price_usd'] = round(float(coin['price_usd']), 2)
            prices.append(item)
        
        return prices