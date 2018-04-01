from abc import ABC, abstractmethod
import requests

class BaseAPIClient(ABC):
    
    def _call(self, url, method='GET'):
        if (method == 'GET'):
            return requests.get(url)
        elif (method == 'POST'):
            pass