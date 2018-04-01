import requests
import json
from exchange.bittrex_api import BittrexAPIClient
from exchange.poloniex_api import PoloniexAPIClient

class Coin():
    
    # Private Class variables (cannot be modified from outside class)
    __coin_list = []
    
    # Coin APIs
    __coinmarketcap_api_url = 'https://api.coinmarketcap.com/v1'
    __coinmarketcap_ticker_path = 'ticker'
    
    # Exchange APIs
    __binance_api_url = 'https://www.binance.com'
    __binance_fees_path = 'assetWithdraw/getAllAsset.html'
    

    
    def __init__(self, ticker, rank, price_usd):
        self.ticker = ticker
        self.rank = rank
        self.price_usd = price_usd
        
        # Each coin will hava a list of exchanges
        #self.exchanges = []
        self.binance_fee = None
        self.binance_fee_usd = None
        

    @staticmethod
    def api_seed (api_id):
        
        if api_id == 'COINMARKETCAP':
            Coin.__coin_list.clear() # Delete old data
            response = requests.get(Coin.__coinmarketcap_api_url + '/' + Coin.__coinmarketcap_ticker_path)
            data = json.loads(response.content.decode('utf-8'))
            for coin in data:
                c = Coin(coin['symbol'], coin['rank'], coin['price_usd'])
                Coin.__coin_list.append(c)

            Coin.__refresh_withdrawal_fees(['BINANCE', 'BITTREX', 'POLONIEX'])


    @staticmethod
    def __refresh_withdrawal_fees(exchanges):
        
        if 'BINANCE' in exchanges:
            bin_response = requests.get(Coin.__binance_api_url + '/' + Coin.__binance_fees_path)
            bin_list = json.loads(bin_response.content.decode('utf-8'))
        
        if 'BITTREX' in exchanges:
            bit = BittrexAPIClient()
            bit_list = bit.get_withdrawal_fees()

        if 'POLONIEX' in exchanges:
            polo = PoloniexAPIClient()
            polo_list = polo.get_withdrawal_fees()
        
        for coin in Coin.__coin_list:
            
            for bin_coin in bin_list:
                if (coin.ticker == bin_coin['assetCode']):
                    coin.binance_fee = bin_coin['transactionFee']
                    coin.binance_fee_usd = round(float(coin.binance_fee) * float(coin.price_usd), 2)
                    break
                
            for bit_coin in bit_list:
                if (coin.ticker == bit_coin['ticker']):
                    coin.bittrex_fee = bit_coin['withdrawal_fee']
                    coin.bittrex_fee_usd = round(float(coin.bittrex_fee) * float(coin.price_usd), 2)
                    break
                
            for polo_coin in polo_list:
                if (coin.ticker == polo_coin['ticker']):
                    coin.poloniex_fee = polo_coin['withdrawal_fee']
                    coin.poloniex_fee_usd = round(float(coin.poloniex_fee) * float(coin.price_usd), 2)
                    break
                
                
    @staticmethod
    def get_json():
        d_list = []
        for c in Coin.__coin_list:
            d_list.append(c.__dict__)
            
        return json.dumps(d_list, separators=(',',':'))

    @staticmethod
    def find_coin(ticker):
        result = None
        for c in Coin.__coin_list:
            if c.ticker == ticker:
                result = c.__dict__
                break
        
        return json.dumps(result, separators=(',',':'))