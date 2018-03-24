import requests
import json

class Coin():
    
    # Private Class variables (cannot be modified from outside class)
    __coin_list = []
    __coinmarketcap_api_url = 'https://api.coinmarketcap.com/v1'
    __coinmarketcap_ticker_path = 'ticker'
    
    def __init__(self, ticker, rank):
        self.ticker = ticker
        self.rank = rank
        
        # Temporary attributes, will be included in Exchange class
        #self.exchanges = []
        self.binance_fee = None
        self.binance_fee_usd = None
        self.bittrex_fee = None
        self.bittrex_fee_usd = None
        self.poloniex_fee = None
        self.poloniex_fee_usd = None
        

    @staticmethod
    def api_seed (api_id):
        
        if api_id == 'COINMARKETCAP':
            Coin.__coin_list.clear() # Delete old data
            response = requests.get(Coin.__coinmarketcap_api_url + '/' + Coin.__coinmarketcap_ticker_path)
            data = json.loads(response.content.decode('utf-8'))
            for coin in data:
                c = Coin(coin['symbol'], coin['rank'])
                Coin.__coin_list.append(c)
            

    @staticmethod
    def get_json():
        d_list = []
        for c in Coin.__coin_list:
            d_list.append(c.__dict__)
            
        return json.dumps(d_list, separators=(',',':'))
