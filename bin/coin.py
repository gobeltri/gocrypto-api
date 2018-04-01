import json

class Coin():
    
    def __init__(self, ticker, rank, price_usd):
        self.ticker = ticker
        self.rank = rank
        self.price_usd = price_usd
        
        # Each coin will hava a list of exchanges
        #self.exchanges = []
        self.binance_fee = None
        self.binance_fee_usd = None
        self.bittrex_fee = None
        self.bittrex_fee_usd = None       
        self.poloniex_fee = None
        self.poloniex_fee_usd = None
        
    def to_json(self) -> dict:
        return json.dumps(self.__dict__, separators=(',',':'))