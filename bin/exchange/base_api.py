from abc import ABC, abstractmethod
import requests

class BaseAPIClient(ABC):
    
    @abstractmethod
    def get_withdrawal_fees(self) -> list:
        """
        Get a list of coins and its withdrawal fees
        :return:
            ticker	[string]
            withdrawal_fee	[float]
        """
    
    def _call(self, url, method='GET'):
        if (method == 'GET'):
            return requests.get(url)
        elif (method == 'POST'):
            pass