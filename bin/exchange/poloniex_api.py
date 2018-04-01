from exchange.base_api import BaseAPIClient
import json

class PoloniexAPIClient(BaseAPIClient):
    
    def __init__(self):
        self.API_URL = 'https://poloniex.com/public'
        self.FEES_PATH = '?command=returnCurrencies'
    
    def get_withdrawal_fees(self) -> list:
        response = self._call(self.API_URL + self.FEES_PATH)
        response_json = json.loads(response.content.decode('utf-8'))
        withdrawal_fees = []
        for key in response_json.keys():
            item = {}
            item['ticker'] = key
            item['withdrawal_fee'] = float(response_json[key]['txFee'])
            withdrawal_fees.append(item)
            
        return withdrawal_fees