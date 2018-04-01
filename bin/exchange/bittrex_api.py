from exchange.base_api import BaseAPIClient
import json

class BittrexAPIClient(BaseAPIClient):
    
    def __init__(self):
        self.API_URL = 'https://bittrex.com/api/v1.1/public'
        self.FEES_PATH = 'getcurrencies'
    
    def get_withdrawal_fees(self) -> list:
        response = self._call(self.API_URL + '/' + self.FEES_PATH)
        response_json = json.loads(response.content.decode('utf-8'))
        withdrawal_fees = []
        for coin in response_json['result']:
            item = {}
            item['ticker'] = coin['Currency']
            item['withdrawal_fee'] = coin['TxFee']
            withdrawal_fees.append(item)
            
        return withdrawal_fees