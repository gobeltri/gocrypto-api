import json
from coin import Coin
from api_client.coinmarketcap import CoinMarketCapAPIClient
from api_client.bittrex import BittrexAPIClient
from api_client.poloniex import PoloniexAPIClient
from api_client.binance import BinanceAPIClient
import ccxt

class CoinList():
    
    COINMARKETCAP = 1
    BINANCE = 2
    BITTREX = 3
    POLONIEX = 4
    KRAKEN = 5
    KUCOIN = 6
    
    def __init__(self):
        self.coin_list = []
    
    def seed(self, source):
        """
        Fills self.coin_list with data from @source
        @source: CoinList.COINMARKETCAP
        """
        if (source == CoinList.COINMARKETCAP):
            self.coin_list.clear()
            cmc = CoinMarketCapAPIClient()
            cmc_coins = cmc.get_prices()
            for cmc_coin in cmc_coins:
                c = Coin(cmc_coin['ticker'], cmc_coin['rank'], cmc_coin['price_usd'])
                self.coin_list.append(c)

    def update_withdrawal_fees(self, exchanges):
        """
        Update withdrawal fees data on self_coin_list
        @exchanges: CoinList.BINANCE | CoinList.BITTREX | CoinList.POLONIEX
        """
        
        bin_list, bit_list, polo_list = [], [], []
        kraken_dict = {}
        
        if CoinList.BINANCE in exchanges:
            bin = BinanceAPIClient()
            bin_list = bin.get_withdrawal_fees()
        
        if CoinList.BITTREX in exchanges:
            bit = BittrexAPIClient()
            bit_list = bit.get_withdrawal_fees()

        if CoinList.POLONIEX in exchanges:
            polo = PoloniexAPIClient()
            polo_list = polo.get_withdrawal_fees()

        if CoinList.KRAKEN in exchanges:
            kraken = ccxt.kraken()
            kraken_dict = kraken.fees['funding']['withdraw']
        
        if CoinList.KUCOIN in exchanges:
            kucoin = ccxt.kucoin()
            kucoin_dict = kucoin.fees['funding']['withdraw']
            
        for coin in self.coin_list:
            for bin_coin in bin_list:
                if (coin.ticker == bin_coin['ticker']):
                    coin.binance_fee = bin_coin['withdrawal_fee']
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
                
            for key,value in kraken_dict.items():
                if (coin.ticker == key ):
                    coin.kraken_fee = value
                    coin.kraken_fee_usd = round(float(coin.kraken_fee) * float(coin.price_usd), 2)
                    break
                
            for key,value in kucoin_dict.items():
                if (coin.ticker == key ):
                    coin.kucoin_fee = value
                    coin.kucoin_fee_usd = round(float(coin.kucoin_fee) * float(coin.price_usd), 2)
                    break
    
    def find_coin(self, ticker) -> Coin:
        for c in self.coin_list:
            if c.ticker == ticker:
                return c
        return None
        
    def to_json(self) -> list:
        d_list = []
        for c in self.coin_list:
            d_list.append(c.__dict__)
            
        return json.dumps(d_list, separators=(',',':'))