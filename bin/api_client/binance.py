from api_client.base import BaseAPIClient
import json

class BinanceAPIClient(BaseAPIClient):
    
    def __init__(self):
        self.API_URL = 'https://www.binance.com'
        self.FEES_PATH = 'assetWithdraw/getAllAsset.html'
    
    def get_withdrawal_fees(self) -> list:
        """
        Get a list of coins and its withdrawal fees
        :return:
            ticker	[string]
            withdrawal_fee	[float]
        """
        response = self._call(self.API_URL + '/' + self.FEES_PATH)
        response_json = json.loads(response.content.decode('utf-8'))
        withdrawal_fees = []
        for coin in response_json:
            item = {}
            item['ticker'] = coin['assetCode']
            item['withdrawal_fee'] = coin['transactionFee']
            withdrawal_fees.append(item)
            
        return withdrawal_fees